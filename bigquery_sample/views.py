import json
from typing import Iterator
from django.http import HttpResponse
from django.http.response import JsonResponse
from google.cloud import bigquery
from google.oauth2 import service_account


project_id = 'earlsproject'
client = bigquery.Client(project = project_id)


def index(request):
    return HttpResponse("Hello, world.")

def hacker_news(request):

    sql = """select title, author, time_ts as Date
    from bigquery-public-data.hacker_news.stories
    order by time_ts desc 
    limit 5;"""

    query = client.query(sql)
    results = query.result()
    records = [dict(row) for row in results]
    response = json.dumps(str(records))

    return HttpResponse(response)


def github(request):

    sql = """select committer.name, count(commit) as Commits
from bigquery-public-data.github_repos.sample_commits
where committer.date between "2016-01-01" and "2016-12-31"
group by committer.name
order by 2 desc;"""

    query = client.query(sql)
    results = query.result()
    records = [dict(row) for row in results]
    response = json.dumps(str(records))

    return HttpResponse(response)
