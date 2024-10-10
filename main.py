#Variables globales
markdown = ""
#Funciones
def run(html: str) -> str:
    # TODO
    global markdown
    #Variables locales
    h1 = "#" * 4
    h2 = "#" * 2
    h3 = "#" * 3

    repetidor = int(html[2]) 
    #El 2 es que coge la posicion de la variable html
    h1 = '#' * repetidor + html[4:8]
    print(h1)
    return markdown

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    