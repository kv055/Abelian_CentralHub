# import Message_Que.find_parent
import json
from External_Infrastructure.Q_PUB_SUB_class import Q
from External_Infrastructure.aws_sql_connect import SQL_Server

# for index,row in enumerate(all_rows):
#     # convert row to JSON
#     json_row = json.dumps(row)
#     entry = {
#         'Id': str(index),
#         'MessageBody': json_row,
#         'DelaySeconds': message_delay,
#         'MessageDeduplicationId': str(index),
#         'MessageGroupId': str(index)
#     }
#     messages_for_q.append(entry)

#     length = len(all_rows) - 1
#     # every 10 elements
#     if index % 9 == 0 and index > 0 or index == length:
#         # push q into the queue
#         # print(messages_for_q)
#         # publish_many(messages_for_q)
#         publish_many_FIFO(messages_for_q)
#         messages_for_q.clear()
#         message_delay += 10

class Insert_config_rows_into_Q:
    def __init__(self):
        # initialise connections to the Q and the DB
        self.que_instance = Q()
        self.db_instance = SQL_Server('DummyData')

    def Live_Trading_construct_deploy_message(self, config_row):
        deploy_message_body = json.dumps(
        {
            'Message_Group': 'Deploy',
            'Config_Row': config_row
        })
        return deploy_message_body

    def Live_Trading_construct_stop_trading_message(self, row_id):
        stop_message_body = json.dumps(
        {
            'Message_Group': 'Stop_Trading',
            'Config_row_Id': row_id
        })
        return stop_message_body

    def Live_Trading_fetch_config_rows(self):
        # Fetch Config rows
        # if row status_active = true but message_id = 0, send 'Deploy' Message
        # if row status_active = false but message_id != 0, send 'Stop_Trading' Message
        
            #         JOIN exchange_keys
            #     ON config_live_trading.keys_id = exchange_keys.id
            # JOIN assets
            #     ON config_live_trading.asset_id = assets.id
                #             assets.data_provider,
                # assets.ticker,
                # assets.live_data_url,
                # assets.live_data_req_body,
                # exchange_keys.exchange_name,
                # exchange_keys.priv_key,
                # exchange_keys.pub_key,
                # exchange_keys.api_endpoint
        
        fetch_config_rows_to_deploy_sql = f"""
            SELECT
                config_live_trading.id,
                config_live_trading.strategy_id,
                config_live_trading.strategy_params,
                config_live_trading.asset_id,
                config_live_trading.keys_id
            FROM config_live_trading
            WHERE status_active = 1 
            -- and message_id is null
        """
        self.db_instance.cursor.execute(fetch_config_rows_to_deploy_sql)
        self.deploy_trading = self.db_instance.cursor.fetchall()

        fetch_config_rows_to_stop_sql = f"""
           SELECT * FROM config_live_trading
           WHERE status_active = 0 and message_id is not null 
        """
        self.db_instance.cursor.execute(fetch_config_rows_to_stop_sql)
        self.stop_trading = self.db_instance.cursor.fetchall()

    def Live_Trading_insert_deploy_messages_into_q(self):
        list_of_messages_to_insert_into_q = []

        if len(self.deploy_trading) > 0:
            for row in self.deploy_trading:
                message_body = self.Live_Trading_construct_deploy_message(row)
                list_of_messages_to_insert_into_q.append({
                    'Body':message_body,
                    'Row_ID': row['id']
                })

        for message in list_of_messages_to_insert_into_q:
            response = self.que_instance.publish(message['Body'])
            # response = self.que_instance.publish_FIFO(message['Body'])
            insert_messageID_sql = f"""
                UPDATE config_live_trading
                SET message_id = '{response['MessageId']}'
                WHERE id = '{message['Row_ID']}'
            """
            self.db_instance.cursor.execute(insert_messageID_sql)
            self.db_instance.connection.commit()

    def Live_Trading_insert_stop_trading_messages_into_q(self):
        list_of_messages_to_insert_into_q = []

        if len(self.stop_trading) > 0:
            for row in self.stop_trading:
                message_body = self.Live_Trading_construct_stop_trading_message(row['id'])
                list_of_messages_to_insert_into_q.append(message_body)

        for message in list_of_messages_to_insert_into_q:
            self.que_instance.publish(message)

