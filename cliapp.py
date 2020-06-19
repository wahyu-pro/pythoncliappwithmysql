import mysql.connector as mysql
import click

class TODOCliApp:
    global cursor
    @click.group()
    def cli():
        """ welcome to my todocliapp """

    @cli.command("list")
    def list():
        # select from todo
        query_select = "select * from todo"
        cursor.execute(query_select)
        for a in cursor:
            Id = a[0]
            name = a[1]
            status = a[2]
            print("{}. {} {}".format(Id, name, status))

    @cli.command("add")
    @click.argument('text', type=str)
    def add(text):
        value = {
            'name' : text,
            'status' : ''
        }
        query_insert = "INSERT INTO todo""(name, status)""values (%(name)s,%(status)s)"
        cursor.execute(query_insert, value)
        connect.commit()

    @cli.command('update')
    @click.argument('id', type=int)
    @click.argument('name', type=str)
    def update(id, name):
        query_update = "UPDATE todo SET name = %s WHERE id = %s"
        data = (name, id)
        cursor.execute(query_update, data)
        connect.commit()

    @cli.command("delete")
    @click.argument('id', type=int)
    def delete(id):
        query_delete = "DELETE FROM todo WHERE id = %s"
        data = (id,)
        cursor.execute(query_delete, data)
        connect.commit()

    @cli.command("clear")
    def clear():
        inp = input("Are you sure want to delete? [\"y\"/\"N\"] ")
        res = inp.lower()
        if inp == "y":
            query_clear = "TRUNCATE TABLE todo"
            cursor.execute(query_clear)
            connect.commit()
        else:
            pass

    @cli.command("done")
    @click.argument('id')
    def done(id):
        query_update = "UPDATE todo SET status = %s WHERE id = %s"
        sett = "(DONE)"
        data = (sett, id)
        cursor.execute(query_update, data)
        connect.commit()

    @cli.command("undone")
    @click.argument('id')
    def undone(id):
        query_update = "UPDATE todo SET status = %s WHERE id = %s"
        sett = ""
        data = (sett, id)
        cursor.execute(query_update, data)
        connect.commit()



if __name__ == "__main__":
    config = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': '',
        'database': 'todocliapp'
        }

    # koneksi 
    connect = mysql.connect(**config)
    cursor = connect.cursor()

    TODOCliApp.cli()