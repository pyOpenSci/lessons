# About this data

The data in this folder were collected using the cross-ref API and the requests library. 

Originally, the plan was to use habanero. However, there were some API requests and rate-limiting issues, so I created a separate workflow to grab the data. 

`joss-publications.json` is a dataset created from the using code in the `joss-pyos-data.md` notebook. Data are grabbed and published by JOSS starting on May 1, 2019, which is close to when pyOS had its first package published via JOSS.



```python
params = {
    'filter': 'type:journal-article,container-title:Journal of Open Source Software,from-pub-date:2019-05-01',
    'rows': 50  # 50 rows per request to match the rate limit / second
}
```

The plan is to create a second, smaller dataset that has some things messed up that people can clean up. 