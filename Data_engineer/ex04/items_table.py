import psycopg2
import os

def create_item_table(table_name, file_path):
    return f"""CREATE TABLE IF NOT EXISTS public.{table_name}
(
    product_id integer,
    category_id bigint,
    category_code character varying,
    brand character varying
);

ALTER TABLE IF EXISTS public.{table_name}
    OWNER TO hasabir;


COPY public.{table_name} FROM '{file_path}' DELIMITER ',' CSV HEADER;
"""



def main():

    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database="piscineds",
        user='hasabir',
        password='mysecretpassword'

    )

    cursor = connection.cursor()

    directory_path = "../data"

    for root, _ , files in os.walk(directory_path):
        current_dir = root.split('/')[-1:][0]
        
        
        for file in files:
            if current_dir == 'item':
                sql = create_item_table(file[:-4], f"/tmp/data/{current_dir}/{file}")

                cursor.execute(sql)
                connection.commit()


    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()