import sys
import psycopg2
import pandas as pd


def cookies_sold(council_name,troop_number):
    try:
        conn = psycopg2.connect("host=courses dbname=z1947594 user=z1947594 password=1997Oct10")
        cur = conn.cursor()
        select_sql = '''select t1.cookie_name, sum(t1.quantity) as box_count, sum(t1.total_price) as total_price_in_dollars
from ((select i.cookie_name, m.troop_number, m.council_name, i.quantity, i.quantity * s.price as total_price
from individual_sales i inner join  member_troop m on i.girl_name = m.name and i.girl_address = m.address
inner join sells_for s on i.cookie_name = s.cookie_name and m.council_name = s.council_name
where m.council_name = (%s) and m.troop_number = (%s))
union
(select sh.cookie_name, sh.troop_number,sh.council_name,sh.quantity, sh.quantity * s.price as total_price
from sells_for s join shop_sales sh on  s.cookie_name = sh.cookie_name and s.council_name = sh.council_name where sh.council_name = (%s) and sh.troop_number = (%s)))t1
group by t1.cookie_name;'''
        cur.execute(select_sql, [council_name,troop_number,council_name,troop_number])
        # conn.commit()
        records = cur.fetchall()
        df = pd.DataFrame(records, columns = ["Cookie_name", "box_count","total_price_in_dollars"])
        print(df)
    except (Exception, psycopg2.Error) as error:
         print("error occures while executing",": ", error)
    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

def main():
    council_name = input("Please enter council_name:")
    troop_number = input("Please enter troop_number:")
    try:
        cookies_sold(council_name,troop_number)
    except Exception as error:
            print("Error occured while reading from: ", error)

if __name__ == "__main__":
   main()
