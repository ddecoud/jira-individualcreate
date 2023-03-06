from jira import JIRA

jira_connection = JIRA(
    basic_auth=('daniela.decoud@gmail.com', 'k'),
    server="https://danidq.atlassian.net"
)

issue_list = [
    {
        'project': {'key': 'PROD'},
        'summary': 'Empezar a segmentar mercado',
        'description': 'Empezar a segmentar mercado',
        'issuetype': {'name': 'Task'},
    },
    {
        'project': {'key': 'PROD'},
        'summary': 'Actualizar script de docu con zabbix',
        'description': 'Actualizar script de docu con zabbix',
        'issuetype': {'name': 'Task'},
    },
    {
        'project': {'key': 'PROD'},
        'summary': 'Encontrar responsable para guides',
        'description': 'Encontrar responsable para guides',
        'issuetype': {'name': 'Task'},
    }]

issues = jira_connection.create_issues(field_list=issue_list)