import webbrowser

user_query = input("Introduce lo que decea buscar:  ")

url= "https://www.google.com/?gws_rd=cr&ssl&ei=dTqZY5yCI_jBkPIPsbubqAE#q=%s" % user_query
'''
gsw = google web server
rd = redirected
cr= country reffered
ssl = protocolo de comunicacion a usar
'''

webbrowser.open_new(url)



