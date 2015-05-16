---
title: Clearing out local Play Framework Dependency Libraries
layout: post 
category: blog
tags: play-framework maven
year: 2015
month: 5
day: 15
published: true
summary: How to clear out local play framework dependency libraries
image: play.svg
---

Play/SBT project in the company has binary dependency on other maven projects built within the company. Typically I am updating code on the maven project and call some of the functionalities through the play framework app. 

A brute force way to make play/sbt pick up new code is to update the version of the maven project and then the app resolves the jar from local '~/.m2/' directory. However this process is ugly and forces too many version updates while testing locally.

A better way is to delete the dependent library from play's cache and force play to download the jar from '~/.m2/' :

    which play
    cd /usr/local/bin/play-2.1.3/repository/cache/
    tree | grep my-project
    rm -rf path-to/my-project

