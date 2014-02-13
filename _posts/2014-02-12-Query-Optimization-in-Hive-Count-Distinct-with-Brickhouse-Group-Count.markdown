---
title: Query Optimization in Hive - Count Distinct with Brickhouse Group Count
layout: post 
category: Engineering
tags: query optimization, hive, brickhouse
year: 2014
month: 2
day: 12
published: true
summary: How to optimize hive count distincts with brickhouse group_count udf.
image: blacktocat.png
---

Suppose you have a big table of all movies ever made and you want to know the count of actors. 
A typical hive query to achieve this is as follows:

    select count(distinct actor_id) as actor_count
    from movies

To determine the set of distinct actor_id, the query gets only one reducer as every single record from table `movies` will be compared against the existing set of actor_id. 
Naturally, this increases the query processing time.

To avoid this bottleneck and optimize the query, we can use Brickhouse's [group_count](https://github.com/klout/brickhouse/blob/master/src/main/java/brickhouse/udf/collect/GroupCountUDF.java) UDF. 
This UDF groups all entries for a given key and assigns an index to each entry in the set of entries. 
For example, if we want to know the debut movie release data for all actors, we can use the follow query:

    select actor_id, movie_id, movie_release_date
    from movies
    distribute by actor_id
    sort by actor_id, movie_release_date
    where group_count(movie_id) = 0;

The `distribute by ..' pattern will make sure data is distributed across many reducers.
Since the above query will return only one entry for a key, we can use this property to rewrite the count distinct query. 
Additionally, we don't care about sorting the data for each entry, so we can get rid of the 'sort by ..' pattern.
Thus the optimized query looks as follows:

    select count(*)
    from
    ( select actor_id, movie_id
      from movies
      distribute by actor_id
      where group_count(movie_id) = 0
    ) a;

