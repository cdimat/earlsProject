import json
from typing import Iterator
from django.http import HttpResponse
from django.http.response import JsonResponse
from google.cloud import bigquery
from google.oauth2 import service_account


project_id = 'earlsproject'
client = bigquery.Client(project = project_id)

def requester(sql):
    query = client.query(sql)
    results = query.result()
    records = [dict(row) for row in results]
    response = json.dumps(str(records))

    return(response)


def index(request):
    return HttpResponse("Hello, world.")

def hacker_news(request):

    sql = """SELECT title, author, time_ts as Date
    FROM bigquery-public-data.hacker_news.stories
    ORDER BY time_ts DESC 
    LIMIT 5;"""

    return HttpResponse(requester(sql))


def github(request):

    sql = """SELECT committer.name, count(commit) as Commits
    FROM bigquery-public-data.github_repos.sample_commits
    WHERE committer.date BETWEEN "2016-01-01" AND "2016-12-31"
    GROUP BY committer.name
    ORDER BY 2 desc;"""

    return HttpResponse(requester(sql))
