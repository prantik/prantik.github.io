---
title: Find Set Difference in Hive 
layout: post 
category: blog
tags: hive
year: 2014
month: 2
day: 15
published: true
summary: How to find set difference in Hive 
image: hive.png
---

Hive doesn't support `NOT IN` patterns in sub query. 
So we can't run this following query:

    select actor_id
    from table1
    where NOT actor_id IN 
      ( select actor_id
        from table2
      );

To achieve the set difference, we have to get a little more creative: 

    select t1.actor_id
    from 
    ( select actor_id
      from table1
    ) t1
    left outer join 
    ( select actor_id
      from table2
    ) t2
    on (t1.actor_id = t2.actor_id)
    where t2.actor_id is null;

Rows where successful joins are possible will have a non-null entry and this way they will be filtered out. The left outer join will make sure all entries from table1 are included and rows from table2 are filtered out. 