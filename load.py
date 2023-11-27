import sys
import psycopg2

def create_dict(col_name_list):
    d = {}

    for i in col_name_list:
        d[i] = None

    return d
    
def build_where_clause(col_names_list):
    new_name_list = []
    for item in col_names_list:
        new_name_list.append(item + " = (%s)")
    return " AND ".join(new_name_list)


def load_data_into_table(table_name, col_names_list, col_values_list):
    try:
        conn = psycopg2.connect("host=courses dbname=z1947594 user=z1947594 password=1997Oct10")
        cur = conn.cursor()
        select_sql = 'SELECT * FROM ' + table_name + ' WHERE ' + build_where_clause(col_names_list)
        cur.execute(select_sql, col_values_list)
        records = cur.fetchall()
        if len(records) == 0:
            insert_sql = 'insert into ' + table_name + ' (' + ','.join(col_names_list) + ') VALUES (' + ','.join(['%s'] * len(col_names_list))+ ')'
            cur.execute(insert_sql, col_values_list)
            conn.commit()
        else:
            pass
            # print("Duplidate data:", count)
    except (Exception, psycopg2.Error) as error:
         print("Failed to insert record into", table_name, ": ", error)
    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()


def process_data_from_file(file_name):
    with open(file_name) as file:
        col_names = file.readline()
        col_name_list = col_names.rstrip().split("|")
        d = create_dict(col_name_list)
        line_number = 1
        for line in file:
            try:
                print("loading line number:", line_number)
                col_values = line.rstrip().split("|")
                for indx, col in enumerate(col_name_list):
                    d[col] = col_values[indx]

                # load girl and leader date into Member table

                if d["Girl Name"] != "":
                    load_data_into_table("member", ["name", "address"], [d["Girl Name"], d["Girl Address"]])
                    load_data_into_table("girl", ["name", "address", "girl_rank"], [d["Girl Name"], d["Girl Address"], d["Girl rank"]])
                    

                load_data_into_table("member", ["name", "address"], [d["Leader Name"], d["Leader Address"]])
                load_data_into_table("leader", ["name", "address"], [d["Leader Name"], d["Leader Address"]])
                load_data_into_table("customer", ["name", "address"], [d["Customer Name"], d["Customer Address"]])
                load_data_into_table("cookie", ["name"], [d["Cookie name"]])
                load_data_into_table("baker", ["name", "address"], [d["Baker Name"], d["Baker Address"]])
                load_data_into_table("council", ["name", "baker_name"], [d["Council Name"], d["Baker Name"]])
                load_data_into_table("service_unit", ["name", "number", "council_name"], [d["Service Unit Name"], d["Service Unit Number"], d["Council Name"]])
                load_data_into_table("troop", ["number", "council_name", "service_unit_num"], [d["Troop Number"], d["Council Name"], d["Service Unit Number"]])
                if d["Girl Name"] != "":
                    load_data_into_table("member_troop", ["name", "address", "troop_number", "council_name", "service_unit_num"], 
                    [d["Girl Name"], d["Girl Address"], d["Troop Number"], d["Council Name"], d["Service Unit Number"]])
                load_data_into_table("member_troop", ["name", "address", "troop_number", "council_name", "service_unit_num"], 
                    [d["Leader Name"], d["Leader Address"], d["Troop Number"], d["Council Name"], d["Service Unit Number"]])
                load_data_into_table("offers", ["cookie_name", "baker_name"], [d["Cookie name"], d["Baker Name"]])
                load_data_into_table("sells_for", ["council_name", "cookie_name", "price"], [d["Council Name"], d["Cookie name"], d["Cookie price"]])
                    
                if d["Girl Name"] == "" and d["Girl Address"] == "" and d["Customer Name"] == "" and d["Customer Address"] == "":
                    # shop sale
                    load_data_into_table("shop_sales", ["cookie_name", "troop_number", "council_name", "service_unit_num", "sold_date", "quantity"],
                        [d["Cookie name"],d["Troop Number"], d["Council Name"],d["Service Unit Number"], d["date sold"], d["quantity sold"]])
                else:
                    # individual sale
                    load_data_into_table("individual_sales", ["cookie_name", "customer_name", "customer_address", "girl_name", "girl_address", "sold_date", "quantity"],
                        [d["Cookie name"], d["Customer Name"], d["Customer Address"], d["Girl Name"], d["Girl Address"], d["date sold"], d["quantity sold"]])
                line_number += 1
            except Exception as error:
                print("Error occured while loading the ", line_number, ": ", error)


def main():
    file_name = input("please enter data file name:")
    try:
        process_data_from_file(file_name)
    except Exception as error:
        print("Error occured while reading from: ", file_name)


if __name__ == "__main__":
   main()
