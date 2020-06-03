#!/usr/bin/env python
# Python3 dep wizard

import hashlib
import sys, sqlite3
import functools, re
import zipfile, os

import click

from runif import *


# Example of a fragment added to the recap
# See https://pyformat.info/
# '{first} {last}'.format(**data)
DEP_DESC="""    {appName}:
      application_name: {appName}
      component_type: 'zconnect_{appType}'
      group_id: 'my.shiny.project'
      artifact_id: '{artifactId}'
      version: '1.0.0-SNAPSHOT'
      """

# aar for api and sar for sevices
PROP_TEMPLATE="""
name=%s
group=my.shiny.project
version=1.0.0-SNAPSHOT
archiveType=%s
"""
def create_gradle_prop(projectName, propfile):
    print("Creating",propfile, "for", projectName)
    # Compute application name
    appName=projectName
    if "-API" in projectName:
        appType="aar"
    else:
        appType="sar"
    actualized_props=PROP_TEMPLATE % (appName, appType)
    with open(propfile,"w") as f:
        f.write(actualized_props)
    data={ "appName": appName.replace('-','_'), "appType": appType, "artifactId":appName}
    dep_desc_fragment=DEP_DESC.format(**data )
    append_if_missed("recap.yml", dep_desc_fragment)

def create_master_recap(fname):
    with open(fname,"w") as f:
        f.write("""
  # Describe ZConnect deploy
recap_data:  
  project_list:
""")


def process(project):
    run_if_missed("recap.yml", create_master_recap)
    run_if_missed(project+"/gradle.properties", lambda f: create_gradle_prop(project, f))

@click.command()
@click.argument("projectdirs", nargs=-1)
def zconnect2gradle(projectdirs):
    """
    Given a set of Zconnect directories
    Create a gradle.properties for each project and try also to build a deployment descriptor.

    Version are fixed to 1.0.0-SNAPSHOT and group is fixed to my.shiny.project
    
    It is able to detect sar or aar via naming convention.
    Bring the entire project name as artifact name    
    """
    for project in projectdirs:
        process(project)


if __name__=="__main__":
    zconnect2gradle()