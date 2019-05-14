"""
__author__ : Karthik
__maintainer__ : Manish  & karthik
__organization__ : Deloitte
"""
from datetime import date
from datetime import datetime

import openpyxl
from flask import json
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, Border, Side


class GenerateVrg:

    def generate_VRG(self, data):
        req_data = data
        now = date.today()
        full = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
        wb = openpyxl.Workbook()
        wb = load_workbook('VRG_template.xlsx')

        wb.template = True
        ws = wb.active
        ws.cell(row=6, column=2).value = 'Last Modified:' + full
        ws.cell(row=6, column=4).value = str(
            ws.cell(row=6, column=4).value) + str(req_data['user_name']).title()
        ws.cell(row=6, column=4).alignment = openpyxl.styles.Alignment(
            horizontal='center', vertical='center', wrap_text=True)
        datestring = datetime.strftime(datetime.now(), ' %Y_%m_%d %HH %MM')
        c = 8
        ws.cell(row=6, column=6).value = str(
            ws.cell(row=6, column=6).value) + str(req_data['project_name']).title()
        fname = req_data['project_name'] + datestring

        for i in range(0, len(req_data['pages'])):
            r = 9
            if 'page_name' in req_data['pages'][i]:
                ws.cell(row=8, column=c).value = str(
                    req_data['pages'][i]['page_name']).upper()
                ws.cell(row = 8 , column= c).alignment = \
                    openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
            if 'page_view' in req_data['pages'][i]:
                ws.cell(
                    row=r, column=c).value = req_data['pages'][i]['page_view']
            # site related stuff
            if 'site_brand' in req_data:
                ws.cell(row=r + 1, column=c).value = req_data['site_brand']
            if 'site_name' in req_data:
                ws.cell(row=r + 2, column=c).value = req_data['site_name']
            if 'site_type' in req_data:
                ws.cell(row=r + 3, column=c).value = req_data['site_type']
            if 'site_environment' in req_data:
                ws.cell(row=r + 4, column=c).value = req_data['site_environment']
            if 'site_app_version' in req_data:
                ws.cell(row=r + 5, column=c).value = req_data['site_app_version']
            if 'site_last_build_date' in req_data:
                ws.cell(
                    row=r + 6, column=c).value = req_data['site_last_build_date']

            if 'page_path' in req_data['pages'][i]:
                ws.cell(
                    row=r + 7, column=c).value = req_data['pages'][i]['page_path']
            
            if 'page_name' in req_data['pages'][i]:
                ws.cell(row=r + 8, column=c).value = req_data['pages'][i]['page_name']

            if 'page_url' in req_data['pages'][i]:
                ws.cell(
                    row=r + 9, column=c).value = req_data['pages'][i]['page_url']
            if 'page_referrer' in req_data['pages'][i]:
                ws.cell(
                    row=r + 10, column=c).value = req_data['pages'][i]['page_referrer']
            if 'page_hierarchy' in req_data['pages'][i]:
                ws.cell(
                    row=r + 11, column=c).value = req_data['pages'][i]['page_hierarchy']
            if 'page_language' in req_data['pages'][i]:
                ws.cell(
                    row=r + 12, column=c).value = req_data['pages'][i]['page_language']
            if 'page_accessibility' in req_data['pages'][i]:
                ws.cell(
                    row=r + 13, column=c).value = req_data['pages'][i]['page_accessibility']

            if 'user_auth_state' in req_data['pages'][i]:
                ws.cell(
                    row=r + 14, column=c).value = req_data['pages'][i]['user_auth_state']
            if 'user_type' in req_data['pages'][i]:
                ws.cell(
                    row=r + 15, column=c).value = req_data['pages'][i]['user_type']
            if 'user_id' in req_data['pages'][i]:
                ws.cell(
                    row=r + 16, column=c).value = req_data['pages'][i]['user_id']

            if 'event_error' in req_data['pages'][i]:
                ws.cell(
                    row=r + 44, column=c).value = req_data['pages'][i]['event_error']
            if 'error_type' in req_data['pages'][i]:
                ws.cell(
                    row=r + 45, column=c).value = req_data['pages'][i]['error_type']
            if 'error_sub_type' in req_data['pages'][i]:
                ws.cell(
                    row=r + 46, column=c).value = req_data['pages'][i]['error_sub_type']
            if 'error_field' in req_data['pages'][i]:
                ws.cell(
                    row=r + 47, column=c).value = req_data['pages'][i]['error_field']
            if 'error_message' in req_data['pages'][i]:
                ws.cell(
                    row=r + 48, column=c).value = req_data['pages'][i]['error_message']
            if 'error_code' in req_data['pages'][i]:
                ws.cell(
                    row=r + 49, column=c).value = req_data['pages'][i]['error_code']
            c = c + 1

        for parent in range(0, len(req_data['forms'])):
            r = 8
            for child in range(0, len(req_data['forms'][parent]['steps'])):
                if 'page_name' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(row=8, column=c).value = str(req_data['forms'][parent]['form_name']).upper().replace(" ","-")+"|"+str(
                        req_data['forms'][parent]['steps'][child]['step_name']).upper().replace(" ","-")
                    ws.cell(row = 8 , column= c).alignment = \
                    openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                if 'page_view' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 1, column=c).value = req_data['forms'][parent]['steps'][child]['page_view']

                if 'site_brand' in req_data:
                    ws.cell(row=r + 2, column=c).value = req_data['site_brand']
                if 'site_name' in req_data:
                    ws.cell(row=r + 3, column=c).value = req_data['site_name']
                if 'site_type' in req_data:
                    ws.cell(row=r + 4, column=c).value = req_data['site_type']
                if 'site_environment' in req_data:
                    ws.cell(
                        row=r + 5, column=c).value = req_data['site_environment']
                if 'site_app_version' in req_data:
                    ws.cell(
                        row=r + 6, column=c).value = req_data['site_app_version']
                if 'site_last_build_date' in req_data:
                    ws.cell(
                        row=r + 7, column=c).value = req_data['site_last_build_date']
                if 'page_path' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 8, column=c).value = req_data['forms'][parent]['steps'][child]['page_path']
                if 'page_name' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(row=r + 9, column=c).value = req_data['forms'][parent]['steps'][child]['page_name']

                if 'page_url' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 10, column=c).value = req_data['forms'][parent]['steps'][child]['page_url']
                if 'page_referrer' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 11, column=c).value = req_data['forms'][parent]['steps'][child]['page_referrer']
                if 'page_hierarchy' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 12, column=c).value = str(req_data['forms'][parent]['steps'][child]['page_hierarchy'])
                if 'page_language' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 13, column=c).value = req_data['forms'][parent]['steps'][child]['page_language']
                if 'page_accessibility' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 14, column=c).value = req_data['forms'][parent]['steps'][child]['page_accessibility']

                if 'user_auth_state' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 15, column=c).value = req_data['forms'][parent]['steps'][child]['user_auth_state']
                if 'user_type' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 16, column=c).value = req_data['forms'][parent]['steps'][child]['user_type']
                if 'user_id' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 17, column=c).value = req_data['forms'][parent]['steps'][child]['user_id']

                if 'form_view' in req_data['forms'][parent]['steps'][child]:
                     if (req_data['forms'][parent]['steps'][child]['form_view'] == 'true'):
                        ws.cell(
                            row=r + 18, column=c).value = req_data['forms'][parent]['steps'][child]['form_view']
                if 'form_submit' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['form_submit'] == 'true'):
                        ws.cell(
                            row=r + 19, column=c).value = req_data['forms'][parent]['steps'][child]['form_submit']
                if 'form_qualify' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['form_qualify'] == 'true'):
                        ws.cell(
                            row=r + 20, column=c).value = req_data['forms'][parent]['steps'][child]['form_qualify']
                if 'form_name' in req_data['forms'][parent]:
                    ws.cell(
                        row=r + 21, column=c).value = str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")
                if 'unique_id' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 22, column=c).value = req_data['forms'][parent]['steps'][child]['unique_id']
                if 'form_step' in req_data['forms'][parent]['steps'][child]:
                     if (req_data['forms'][parent]['steps'][child]['form_step'] == 'true'):
                        ws.cell(
                            row=r + 23, column=c).value = req_data['forms'][parent]['steps'][child]['form_step']

                if 'step_name' in req_data['forms'][parent]['steps'][child]:
                    if(req_data['forms'][parent]['steps'][child]['step_name'] != ''):
                        ws.cell(
                            row=r + 24, column=c).value = str(req_data['forms'][parent]['steps'][child]['step_name']).lower().replace(" ","-")
                    else:
                        arr = str(req_data['forms'][parent]['steps'][child]['page_hierarchy']).replace("\\"," ").replace("[","").replace("]","").replace("'","").split(" ")
                        ws.cell(
                            row=r + 24, column=c).value = str(arr[len(arr)-1]).lower().replace(" ","-")

                if 'event_error' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 45, column=c).value = req_data['forms'][parent]['steps'][child]['event_error']
                if 'error_type' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 46, column=c).value = req_data['forms'][parent]['steps'][child]['error_type']
                if 'error_sub_type' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 47, column=c).value = req_data['forms'][parent]['steps'][child]['error_sub_type']
                if 'error_field' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 48, column=c).value = req_data['forms'][parent]['steps'][child]['error_field']
                if 'error_message' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 48, column=c).value = req_data['forms'][parent]['steps'][child]['error_message']
                if 'error_code' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 50, column=c).value = req_data['forms'][parent]['steps'][child]['error_code']

                if req_data['forms'][parent]['is_transaction_exist']:
                    if 'transaction_id' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 29, column=c).value = req_data['forms'][parent]['steps'][child]['transaction_id']
                    if 'transaction_amount' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 30, column=c).value = req_data['forms'][parent]['steps'][child]['transaction_amount']
                    if 'transaction_service_fee' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 31, column=c).value = req_data['forms'][parent]['steps'][child]['transaction_service_fee']
                    if 'transaction_unit' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 32, column=c).value = req_data['forms'][parent]['steps'][child]['transaction_unit']
                    if 'from_transaction' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 34, column=c).value = req_data['forms'][parent]['steps'][child]['from_transaction']
                    if 'to_transaction' in req_data['forms'][parent]['steps'][child]:
                        ws.cell(
                            row=r + 35, column=c).value = req_data['forms'][parent]['steps'][child]['to_transaction']
                    if 'is_external' in req_data['forms'][parent]:
                        ws.cell(
                            row=r + 36, column=c).value = req_data['forms'][parent]['steps'][child]['is_external']
                    if 'is_transaction_complete' in req_data['forms'][parent]:
                        ws.cell(
                            row=r + 37, column=c).value = req_data['forms'][parent]['steps'][child]['is_transaction_complete']

                # Product Specific Details
                if 'product_id' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 87, column=c).value = req_data['forms'][parent]['steps'][child]['product_id']
                if 'product_positioning' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 89, column=c).value = req_data['forms'][parent]['steps'][child]['product_positioning']
                if 'product_grouping' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 90, column=c).value = req_data['forms'][parent]['steps'][child]['product_grouping']
                if 'parent_product' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 91, column=c).value = req_data['forms'][parent]['steps'][child]['parent_product']
                if 'fulfillment' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 81, column=c).value = req_data['forms'][parent]['steps'][child]['fulfillment']
                if 'adjudication' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 93, column=c).value = req_data['forms'][parent]['steps'][child]['adjudication']
                if 'product_recommendation' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['product_recommendation'] == 'true'):
                        ws.cell(
                            row=r + 79, column=c).value = req_data['forms'][parent]['steps'][child]['product_recommendation']
                if 'is_paperless' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['is_paperless'] == 'true'):
                        ws.cell(
                            row=r + 96, column=c).value = req_data['forms'][parent]['steps'][child]['is_paperless']
                if 'summary' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['summary'] == 'true'):
                        ws.cell(
                            row=r + 80, column=c).value = req_data['forms'][parent]['steps'][child]['summary']
                if 'confirmation' in req_data['forms'][parent]['steps'][child]:
                     if (req_data['forms'][parent]['steps'][child]['confirmation'] == 'true'):
                        ws.cell(
                            row=r + 83, column=c).value = req_data['forms'][parent]['steps'][child]['confirmation']
                if 'terms_and_condition' in req_data['forms'][parent]['steps'][child]:
                     if (req_data['forms'][parent]['steps'][child]['terms_and_condition'] == 'true'):
                        ws.cell(
                            row=r + 82, column=c).value = req_data['forms'][parent]['steps'][child]['terms_and_condition']
                if 'personal_details' in req_data['forms'][parent]['steps'][child]:
                    if (req_data['forms'][parent]['steps'][child]['personal_details'] == 'true'):
                        ws.cell(
                            row=r + 78, column=c).value = req_data['forms'][parent]['steps'][child]['personal_details']


                # Error Information in VRG
                if 'event_error' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 45, column=c).value = req_data['forms'][parent]['steps'][child]['event_error']
                if 'error_type' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 46, column=c).value = req_data['forms'][parent]['steps'][child]['error_type']
                if 'error_sub_type' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 47, column=c).value = req_data['forms'][parent]['steps'][child]['error_sub_type']
                if 'error_field' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 48, column=c).value = req_data['forms'][parent]['steps'][child]['error_field']
                if 'error_message' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 49, column=c).value = req_data['forms'][parent]['steps'][child]['error_message']
                if 'error_code' in req_data['forms'][parent]['steps'][child]:
                    ws.cell(
                        row=r + 50, column=c).value = req_data['forms'][parent]['steps'][child]['error_code']
                c = c + 1

        for i in range(0, len(req_data['interaction'])):
            r = 9
            if 'interaction_name' in req_data['interaction'][i]:
                ws.cell(
                    row=8, column=c).value = str(req_data['interaction'][i]['interaction_name']).upper().replace(" ","-").replace(":","-")
                ws.cell(row = 8 , column= c).alignment = \
                    openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
            if 'page_view' in req_data['interaction'][i]:
                ws.cell(
                    row=r, column=c).value = req_data['interaction'][i]['page_view']

            # site related stuff
            if 'site_brand' in req_data:
                ws.cell(row=r + 1, column=c).value = req_data['site_brand']
            if 'site_name' in req_data:
                ws.cell(row=r + 2, column=c).value = req_data['site_name']
            if 'site_type' in req_data:
                ws.cell(row=r + 3, column=c).value = req_data['site_type']
            if 'site_environment' in req_data:
                ws.cell(row=r + 4, column=c).value = req_data['site_environment']
            if 'site_app_version' in req_data:
                ws.cell(row=r + 5, column=c).value = req_data['site_app_version']
            if 'site_last_build_date' in req_data:
                ws.cell(
                    row=r + 6, column=c).value = req_data['site_last_build_date']


            if 'page_path' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 7, column=c).value = req_data['interaction'][i]['page_path']
            if 'page_name' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 8, column=c).value = req_data['interaction'][i]['page_name']
            if 'page_url' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 9, column=c).value = req_data['interaction'][i]['page_url']
            if 'page_referrer' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 10, column=c).value = req_data['interaction'][i]['page_referrer']
            if 'page_hierarchy' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 11, column=c).value = req_data['interaction'][i]['page_hierarchy']
            if 'page_language' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 12, column=c).value = req_data['interaction'][i]['page_language']
            if 'page_accessibility' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 13, column=c).value = req_data['interaction'][i]['page_accessibility']

            if 'user_auth_state' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 14, column=c).value = req_data['interaction'][i]['user_auth_state']
            if 'user_type' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 15, column=c).value = req_data['interaction'][i]['user_type']
            if 'user_id' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 16, column=c).value = req_data['interaction'][i]['user_id']

            if 'site_interaction_event' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 55, column=c).value = req_data['interaction'][i]['site_interaction_event']
            if 'interaction_name' in req_data['interaction'][i]:
                ws.cell(
                    row=r + 56, column=c).value = req_data['interaction'][i]['interaction_name']
            c = c + 1

        for i in range(0, len(req_data['download'])):
            r = 9
            if 'page_name' in req_data['download'][i]:
                ws.cell(
                    row=8, column=c).value = str(req_data['download'][i]['download_file_name']).upper().replace(" ","-").replace(":","-")
                ws.cell(row = 8 , column= c).alignment = \
                    openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
            if 'page_view' in req_data['download'][i]:
                ws.cell(
                    row=r, column=c).value = req_data['download'][i]['page_view']

            # site related stuff
            if 'site_brand' in req_data:
                ws.cell(row=r + 1, column=c).value = req_data['site_brand']
            if 'site_name' in req_data:
                ws.cell(row=r + 2, column=c).value = req_data['site_name']
            if 'site_type' in req_data:
                ws.cell(row=r + 3, column=c).value = req_data['site_type']
            if 'site_environment' in req_data:
                ws.cell(row=r + 4, column=c).value = req_data['site_environment']
            if 'site_app_version' in req_data:
                ws.cell(row=r + 5, column=c).value = req_data['site_app_version']
            if 'site_last_build_date' in req_data:
                ws.cell(
                    row=r + 6, column=c).value = req_data['site_last_build_date']

            if 'page_path' in req_data['download'][i]:
                ws.cell(
                    row=r + 7, column=c).value = req_data['download'][i]['page_path']
            if 'page_name' in req_data['download'][i]:
                ws.cell(
                    row=r + 8, column=c).value = req_data['download'][i]['page_name']
            if 'page_url' in req_data['download'][i]:
                ws.cell(
                    row=r + 9, column=c).value = req_data['download'][i]['page_url']
            if 'page_referrer' in req_data['download'][i]:
                ws.cell(
                    row=r + 10, column=c).value = req_data['download'][i]['page_referrer']
            if 'page_hierarchy' in req_data['download'][i]:
                ws.cell(
                    row=r + 11, column=c).value = req_data['download'][i]['page_hierarchy']
            if 'page_language' in req_data['download'][i]:
                ws.cell(
                    row=r + 12, column=c).value = req_data['download'][i]['page_language']
            if 'page_accessibility' in req_data['download'][i]:
                ws.cell(
                    row=r + 13, column=c).value = req_data['download'][i]['page_accessibility']

            if 'user_auth_state' in req_data['download'][i]:
                ws.cell(
                    row=r + 14, column=c).value = req_data['download'][i]['user_auth_state']
            if 'user_type' in req_data['download'][i]:
                ws.cell(
                    row=r + 15, column=c).value = req_data['download'][i]['user_type']
            if 'user_id' in req_data['download'][i]:
                ws.cell(
                    row=r + 16, column=c).value = req_data['download'][i]['user_id']

            if 'event_error' in req_data['download'][i]:
                ws.cell(
                    row=r + 44, column=c).value = req_data['download'][i]['event_error']

            if 'events_download' in req_data['download'][i]:
                ws.cell(
                    row=r + 50, column=c).value = req_data['download'][i]['events_download']
            if 'download_file_name' in req_data['download'][i]:
                ws.cell(
                    row=r + 51, column=c).value = req_data['download'][i]['download_file_name']
            if 'download_file_type' in req_data['download'][i]:
                ws.cell(
                    row=r + 52, column=c).value = req_data['download'][i]['download_file_type']
            c = c + 1

        if req_data['mobile_json'] == 'True':
            self.json_file(data, wb)
        if req_data['test_case'] == 'True':
            self.testCaseVRG(data,wb)
            self.testCaseMobileJSON(data,wb)

        wb.save(fname + '.xltx')
        return print('success')

    def json_file(self, req_data, wb):
        pages = {}
        for i in range(0, len(req_data['pages'])):
            if 'application_type' in req_data:
                if 'page_name' in req_data['pages'][i]:
                    pages['state_' + req_data['pages'][i]
                    ['page_name'] + ''] = {}
                    pages['state_' + req_data['pages'][i]
                    ['page_name'] + '']['page'] = {}
                    pages['state_' + req_data['pages'][i]['page_name'] + '']['page']['name'] = req_data['pages'][i][
                        'page_name']
                    pages['state_' + req_data['pages'][i]['page_name'] + '']['page']['hierarchy'] = \
                        str(req_data['pages'][i]['page_hierarchy']).replace("'","").replace("[","").replace("]","").replace(" ","-").replace(".",">")
        interaction = {}
        for i in range(0, len(req_data['interaction'])):
            if 'application_type' in req_data:
                if 'interaction_name' in req_data['interaction'][i]:
                    interaction['action_' + str(req_data['interaction'][i]
                    ['interaction_name']).lower().replace(" ","-").replace(":","-") + ''] = {}
                    interaction['action_' + str(req_data['interaction'][i]
                    ['interaction_name']).lower().replace(" ","-").replace(":","-") + '']['interaction'] = {}
                    interaction['action_' + str(req_data['interaction'][i]['interaction_name']).lower().replace(" ","-").replace(":","-") + '']['interaction'][
                        'name'] = str(req_data['interaction'][i]
                    ['interaction_name']).lower().replace(" ","-")

        forms = {}
        for parent in range(0, len(req_data['forms'])):
            for child in range(0, len(req_data['forms'][parent]['steps'])):
                if 'page_name' in req_data['forms'][parent]['steps'][child]:
                    forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-")+ ''] = {}

                    # Product Object Created in Form JSON Object
                    if req_data['forms'][parent]['is_product_exist']:
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'] = [{}]
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['id'] = \
                           str(req_data['forms'][parent]['steps'][child]['product_id']).lower().replace(" ","-")
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['positioning'] = \
                           str(req_data['forms'][parent]['steps'][child]['product_positioning']).lower().replace(" ","-")
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['grouping'] = \
                            str(req_data['forms'][parent]['steps'][child]['product_grouping']).lower().replace(" ","-")
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['parentproduct'] = \
                            str(req_data['forms'][parent]['steps'][child]['parent_product']).lower()
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['adjudication'] = \
                            str(req_data['forms'][parent]['steps'][child]['adjudication']).lower()
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['fulfilment'] = \
                            str(req_data['forms'][parent]['steps'][child]['fulfillment']).lower()
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['product'][0]['paperless'] = \
                            str(req_data['forms'][parent]['steps'][child]['is_paperless']).lower()
                        
                    if req_data['forms'][parent]['is_transaction_exist']:
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'] = [{}]
                        
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['id'] = \
                           str(req_data['forms'][parent]['steps'][child]['transaction_id']).lower().replace(" ","-")

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'] = [{}]

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'][0]['from'] = \
                            str(req_data['forms'][parent]['steps'][child]['from_transaction']).lower().replace(" ","-")

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'][0]['to'] = \
                            str(req_data['forms'][parent]['steps'][child]['to_transaction']).lower().replace(" ","-")

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'][0]['amount'] = \
                            str(req_data['forms'][parent]['steps'][child]['transaction_amount']).lower().replace(" ","-")

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'][0]['unit'] = \
                            str(req_data['forms'][parent]['steps'][child]['transaction_unit']).lower().replace(" ","-")

                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['transaction'][0]['items'][0]['is_external'] = \
                            str(req_data['forms'][parent]['steps'][child]['is_external']).lower().replace(" ","-")
                        
                    # Page Object Created in Form JSON Object
                    forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['page'] = {}
                    forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['page']['hierarchy'] = \
                        str(req_data['forms'][parent]['steps'][child]['page_hierarchy']).replace("\\","").replace("[","").replace("]","").replace("'","").replace(",",">")
                    if req_data['forms'][parent]['steps'][child]['step_name'] != '':
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['page']['name'] = \
                            str(req_data['forms'][parent]['steps'][child]['step_name']).lower().replace(" ","-")
                    else:
                        arr = str(req_data['forms'][parent]['steps'][child]['page_hierarchy']).replace("\\"," ").replace("[","").replace("]","").replace("'","").split(" ")
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['page']['name']= \
                        str(arr[len(arr)-1]).lower().replace(" ","-")

                    # Form Object Created in Form JSON Object
                    forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['form'] = {}
                    forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['form']['name'] = \
                        str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")
                    if req_data['forms'][parent]['steps'][child]['step_name'] != '':
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['form']['step_name'] = \
                        str(req_data['forms'][parent]['steps'][child]['step_name']).replace(" ","-").replace(".",">")
                    else:
                        arr = str(req_data['forms'][parent]['steps'][child]['page_hierarchy']).replace("\\"," ").replace("[","").replace("]","").replace("'","").split(" ")
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['form']['step_name'] = \
                        str(arr[len(arr)-1]).lower().replace(" ","-")

                    # Event Object created in Form JSON Object
                    forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['events'] = {}
                    if (req_data['forms'][parent]['steps'][child]['form_step'] == 'true'):
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['events'][
                            'formstep'] = \
                            str(req_data['forms'][parent]['steps'][child]['form_step']).lower()
                    if (req_data['forms'][parent]['steps'][child]['form_view'] == 'true'):
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['events'][
                            'formview'] = \
                            str(req_data['forms'][parent]['steps'][child]['form_view']).lower()
                    if req_data['forms'][parent]['steps'][child]['form_qualify'] == 'true':
                        forms['state_' + str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['events'][
                            'formqualify'] = \
                            str(req_data['forms'][parent]['steps'][child]['form_qualify']).lower()
                    if req_data['forms'][parent]['steps'][child]['form_submit'] == 'true':
                        forms['state_' +str(req_data['forms'][parent]['form_name']).lower().replace(" ","-")+"-"+str(req_data['forms'][parent]['steps']
                        [child]['step_name']).lower().replace(" ","-") + '']['events'][
                            'form_submit'] = \
                            str(req_data['forms'][parent]['steps'][child]['form_submit']).lower()

        dictMerge = {**forms, **pages, **interaction}
        with open('JsonData.json', 'w') as outfile:
            json.dump(dictMerge, outfile)
        ws1 = wb.create_sheet("JSON File", 1)
        ws1.cell(row=1, column=1).value = json.dumps(dictMerge)
        ws1.row_dimensions[0].height = 300
        ws1.column_dimensions['B'].width = 300
        ws1.cell(row=1, column=1).font = Font(size=12, name='Times New Roman')

    def testCaseVRG(self, req_data,workbook):

        alignment = Alignment(horizontal='left',vertical='top',wrapText=True)
        now = date.today()
        full = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

        ws1 = workbook.create_sheet("VRG Test Cases",2)
        ws1.row_dimensions[1].height = 34.5

        ws1.cell(row = 1 , column= 1).value = 'Sr. No.'
        ws1.cell(row = 1 , column= 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
        ws1.cell(row = 1 , column= 2).value = 'Date Created'
        ws1.cell(row = 1 , column= 3).value = 'Subject'
        ws1.cell(row = 1 , column= 4).value = 'Test Case Name'
        ws1.cell(row = 1 , column= 5).value = 'Test Objective'
        ws1.cell(row = 1 , column= 6).value = 'Step Name'
        ws1.cell(row = 1 , column= 7).value = 'Description'
        ws1.cell(row = 1 , column= 8).value = 'Expected Result'
        ws1.cell(row = 1 , column= 9).value = 'Author'
        for i in range(1,10):
             ws1.cell(row = 1 , column= i).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
             ws1.cell(row = 1 , column= i).font = Font(bold=True,color='008000')

        ws1.column_dimensions['B'].width = 10
        ws1.column_dimensions['D'].width = 30
        ws1.column_dimensions['F'].width = 30
        ws1.column_dimensions['E'].width = 14.89
        ws1.column_dimensions['G'].width = 25
        ws1.column_dimensions['H'].width = 120

        id = 1
        r = 2
        c = 1
        s = 'Step'
        e = 'To Verify Adobe variables match those detailed in the VRG \n \n Pre Condition: Debugger tool to be launched for testing purpose(Recommended  Adobe Pulse Debugger)'
        g = 'Ensure Adobe Debugger is active'

        for i in range(0, len(req_data['pages'])):
            event = 'Events: '
            comment = ' //'
            if 'page_name' in req_data['pages'][i]:
                ws1.cell(row=r, column=c).value = str(id)
                ws1.cell(row = r , column= c).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 1).value = full
                ws1.cell(row=r, column=c + 1).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)

                ws1.cell(row=r, column=c + 2).value = req_data['project_name']
                ws1.cell(row=r, column=c + 2).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 4).value = e
                ws1.cell(row=r, column=c + 4).alignment = openpyxl.styles.Alignment(horizontal='left', vertical='center', wrap_text=True)

                ws1.cell(row=r, column=c + 6).value = g
                ws1.cell(row=r, column=c + 6).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)

                val = req_data['pages'][i]['page_name']
                b = '-.'
                for char in b:
                    val = val.replace(char, " ")
                ws1.cell(row=r, column=c + 3).value = val.title()
                ws1.cell(row=r, column=c + 5).value = req_data['pages'][i]['page_name']

                ws1.cell(row=r, column=c + 3).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 5).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 5).font = openpyxl.styles.Font(bold=True)

            if 'site_brand' in req_data:
                if (bool(req_data['pages'][i]['login_event'])):
                    event = event + ' event19 ,'
                    comment = comment + 'Login Event, '
                if (bool(req_data['pages'][i]['event_error'])):
                    event = event + 'event3'
                    comment = comment + 'Error Event '
                dct = 'page_name, eVar10: ' + str(
                    req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                    req_data['pages'][i]['page_name']) + '    //Unique for each Page' + '\n eVar11: ' + str(
                    req_data['site_app_version']) + ':' + str(req_data['site_last_build_date']) + ':' + str(
                    req_data['site_name']) + ':' + str(req_data[
                                                          'site_type']) + '    //site_app_version,site_last_build_date,site_name,site_type' + '\neVar15: ' + str(
                    req_data['pages'][i]['page_url']) + '    //Page URL' + '\n eVar9: ' + str(
                    req_data['pages'][i]['page_referrer']) + '    //Previous Page Name' + '\n eVar14: ' + str(
                    req_data['pages'][i]['page_hierarchy']) + '    // Hierarchy of the Page' + '\n eVar16: ' + str(
                    req_data['pages'][i]['page_language']) + '    // Language Supported For Page' + '\n prop12: ' + str(
                    req_data['pages'][i]['page_accessibility']) + '\n eVar19: {' + str(
                    req_data['pages'][i]['user_auth_state']) + ' : ' + str(
                    req_data['pages'][i][
                        'user_type']) + '}' + '    // Authentication of User and User Type' + '\n eVar20: ' + str(
                    req_data['pages'][i]['user_id']) + '    // User ID'
                ws1.cell(row=r, column=c + 7).value = str(dct)
                ws1.cell(row=r, column=c + 7).alignment = alignment
                ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.row_dimensions[r].height = 180
            id = id + 1
            r = r + 1

        for i in range(0, len(req_data['interaction'])):
            event = 'Events: '
            comment = ' '
            if 'page_name' in req_data['interaction'][i]:
                ws1.cell(row=r, column=c).value = str(id)
                ws1.cell(row = r , column= c ).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                ws1.cell(row=r, column=c + 1).value = full
                ws1.cell(row = r , column= c + 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                ws1.cell(row=r, column=c + 2).value = req_data['project_name']
                ws1.cell(row = r , column= c + 2).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 4).value = e
                ws1.cell(row = r , column= c + 4).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)

                ws1.cell(row=r, column=c +6).value = g
                ws1.cell(row = r , column= c + 6).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                val = req_data['interaction'][i]['interaction_name']
                b = '-.'
                for char in b:
                    val = val.replace(char, " ")
                ws1.cell(row=r, column=c + 3).value = val.title()
                ws1.cell(row = r , column= c + 3).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 5).value = req_data['interaction'][i]['interaction_name']
                ws1.cell(row = r , column= c + 5).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)

            if 'site_brand' in req_data:
                if bool(req_data['interaction'][i]["site_interaction_event"]):
                    event = event + ' event24 ,'
                    comment = comment + '// Site Interaction Event, '
                dct = 'page_name, eVar10: ' + str(
                    req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                    req_data['interaction'][i]['page_name']) + '    //Unique for each Page' + '\n eVar11: ' + str(
                    req_data['site_app_version']) + ':' + str(req_data['site_last_build_date']) + ':' + str(
                    req_data['site_name']) + ':' + str(req_data[
                                                          'site_type']) + '    //site_app_version,site_last_build_date,site_name,site_type' + '\n eVar15: ' + str(
                    req_data['interaction'][i]['page_url']) + '    //Page URL' + '\n eVar9: ' + str(
                    req_data['interaction'][i]['page_referrer']) + '    //Previous Page Name' + '\n eVar14: ' + str(
                    req_data['interaction'][i]['page_hierarchy']) + '    // Hierarchy of the Page' + '\n eVar16: ' + str(
                    req_data['interaction'][i][
                        'page_language']) + '    // Language Supported For Page' + '\n prop12: ' + str(
                    req_data['interaction'][i]['page_accessibility']) + '' + '\n eVar24: ' + str(
                    req_data['interaction'][i]['interaction_name']) + " //Interaction Name \n" + event + '\t' + comment
                ws1.cell(row=r, column=c + 7).value = str(dct)
                ws1.cell(row=r, column=c + 7).alignment= alignment
                ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.row_dimensions[r].height = 180
            id = id + 1
            r = r + 1

        for i in range(0, len(req_data['download'])):
            event = ''
            comment = ''
            if 'page_name' in req_data['download'][i]:
                ws1.cell(row=r, column=c).value = str(id)
                ws1.cell(row = r , column= c).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                ws1.cell(row=r, column=c + 1).value = full
                ws1.cell(row = r , column= c + 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                ws1.cell(row=r, column=c + 2).value = req_data['project_name']
                ws1.cell(row = r , column= c + 2).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 4).value = e
                ws1.cell(row = r , column= c + 4).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)

                ws1.cell(row=r, column=c + 6).value = g
                ws1.cell(row = r , column= c + 6).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                val = req_data['download'][i]['download_file_name']
                b = '-.'
                for char in b:
                    val = val.replace(char, " ")
                ws1.cell(row=r, column=c + 3).value = val.title()
                ws1.cell(row = r , column= c + 3).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)

                ws1.cell(row=r, column=c + 5).value = req_data['download'][i]['download_file_name']
                ws1.cell(row = r , column= c + 5).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 5).font = openpyxl.styles.Font(bold=True)

            if 'site_brand' in req_data:
                if (bool(req_data['download'][i]['events_download'])):
                    event = event + ' event21 ,'
                    comment = comment + '// Download Event, '
                dct = 'page_name, eVar10: ' + str(
                    req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                    req_data['download'][i]['page_name']) + '    //Unique for each Page' + '\n eVar11: ' + str(
                    req_data['site_app_version']) + ':' + str(req_data['site_last_build_date']) + ':' + str(
                    req_data['site_name']) + ':' + str(req_data[
                                                          'site_type']) + '    //site_app_version,site_last_build_date,site_name,site_type' + '\n eVar15: ' + str(
                    req_data['download'][i]['page_url']) + '    //Page URL' + '\n eVar9: ' + str(
                    req_data['download'][i]['page_referrer']) + '    //Previous Page Name' + '\n eVar14: ' + str(
                    req_data['download'][i]['page_hierarchy']) + '    // Hierarchy of the Page' + '\n eVar16: ' + str(
                    req_data['download'][i][
                        'page_language']) + '    // Language Supported For Page' + '\n prop12: ' + str(
                    req_data['download'][i]['page_accessibility']) + '\n eVar19: {' + str(
                    req_data['download'][i]['user_auth_state']) + ' : ' + str(
                    req_data['download'][i][
                        'user_type']) + '}' + '    // Authentication of User and User Type' + '\n eVar20: ' + str(
                    req_data['download'][i]['user_id']) + '    // User ID' + '\n eVar24: ' + str(
                    req_data['download'][i]['download_file_name']) + ':' + str(req_data['download'][i][
                                                                                  'download_file_type']) + '    // Download FileName:FileType \n' + event + '\t' + comment
                ws1.cell(row=r, column=c + 7).value = str(dct)
                ws1.cell(row = r , column= c + 7).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)

                ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                ws1.row_dimensions[r].height = 180
            id = id + 1
            r = r + 1

        for parent in range(0, len(req_data['forms'])):
            for child in range(0, len(req_data['forms'][parent]['steps'])):
                event = 'Events'
                comment = ''
                if (bool(req_data['forms'][parent]['steps'][child]['form_step'])):
                    event = event + 'event4'
                if (bool(req_data['forms'][parent]['steps'][child]['form_view'])):
                    event = event + ', event1'
                if (bool(req_data['forms'][parent]['steps'][child]['form_submit'])):
                    event = event + ', event2'
                if (bool(req_data['forms'][parent]['steps'][child]['form_qualify'])):
                    event = event + ', event5'
                if (bool(req_data['forms'][parent]['steps'][child]['is_external'])):
                    event = event + ', event46'
                if (bool(req_data['forms'][parent]['steps'][child]['page_login'])):
                    event = event + ', event19'
                if (bool(req_data['forms'][parent]['steps'][child]['event_error'])):
                    event = event + ', event3'
                if (bool(req_data['forms'][parent]['steps'][child]['is_paperless'])):
                    event = event + ', event30'
                if (bool(req_data['forms'][parent]['steps'][child]['product_recommendation'])):
                    event = event + ', event103'

                if 'page_name' in req_data['forms'][parent]['steps'][child]:
                    ws1.cell(row=r, column=c).value = req_data['forms'][parent]['steps'][child]['page_name']
                    ws1.cell(row = r , column= c).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    ws1.cell(row=r, column=1).value = str(id)
                    ws1.cell(row = r , column= 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    ws1.cell(row=r, column=2).value = full
                    ws1.cell(row = r , column= 2).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row=r, column=2).font = openpyxl.styles.Font(bold=True)

                    ws1.cell(row=r, column=3).value = req_data['project_name']
                    ws1.cell(row = r , column= 3).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row=r, column=3).font = openpyxl.styles.Font(bold=True)

                    ws1.cell(row=r, column=5).value = e
                    ws1.cell(row = r , column= 5).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    ws1.cell(row=r, column=7).value = g
                    ws1.cell(row = r , column= 7).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    val = req_data['forms'][parent]['steps'][child]['page_name']
                    b = '-.'
                    for char in b:
                        val = val.replace(char, " ")

                    ws1.cell(row=r, column=4).value = val.title()
                    ws1.cell(row = r , column= 4).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    ws1.cell(row=r, column=6).value = val.title()
                    ws1.cell(row = r , column= 6).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)

                    dt = 'page_name, eVar10: ' + str(
                        req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_name']) + '    //Unique for each Page \n eVar11:' + str(
                        req_data['site_app_version']) + ':' + str(req_data['site_last_build_date']) + ':' + str(
                        req_data['site_name']) + ':' + str(req_data[
                                                              'site_type']) + '    //site_app_version:site_last_build_date:site_name:site_type' + '\n eVar15: ' + str(
                        req_data['forms'][parent]['steps'][child]['page_url']) + '    //Page URL' + '\n eVar9: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_referrer']) + ' //Previous Page Name' + '\n eVar14: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_hierarchy']) + ' // Hierarchy of the Page' + '\n eVar16: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_language']) + '    // Language Supported For Page' + '\n prop12: ' + str(
                        req_data['forms'][parent]['steps'][child]['page_accessibility']) + '\n eVar19: {' + str(
                        req_data['forms'][parent]['steps'][child]['user_auth_state']) + ' : ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'user_type']) + '}' + ' // Authentication of User and User Type ' + '\n eVar20: ' + str(
                        req_data['forms'][parent]['steps'][child]['user_id']) + ' // User ID' + '\n evar1: ' + str(
                        req_data['forms'][parent]['form_name']) + ' // Form Name' + '\n eVar4: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'step_name']) + ' //Form Step Name' + ' \n eVar5: ' + str(
                        req_data['forms'][parent]['steps'][child]['unique_id']) + ' // Unique Id of Form'
                    if (req_data['forms'][parent]['is_transaction_exist']):
                        dt = dt + '\n eVar41: ' + str(
                            req_data['forms'][parent]['steps'][child]['from_transaction']) + ':' + str(
                            req_data['forms'][parent]['steps'][child][
                                'to_transaction']) + '    //Transaction From: Transaction To'
                    if (req_data['forms'][parent]['is_product_exist']):
                        dt = dt + '\n eVar82: ' + str(req_data['forms'][parent]['steps'][child][
                                                          'product_positioning']) + '    //Product Positioning \n eVar83 : ' + str(
                            req_data['forms'][parent]['steps'][child][
                                'product_grouping']) + '    //Product grouping \n eVar84: ' + str(
                            req_data['forms'][parent]['steps'][child][
                                'parent_product']) + ' // Parent Product \neVar88:' + str(
                            req_data['forms'][parent]['steps'][child]['adjudication']) + '   // Adjudication\n ' + event
                    ws1.cell(row=r, column=c + 7).value = str(dt)
                    ws1.cell(row = r , column= c+7).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                    ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                    ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.row_dimensions[r].height = 203
                    #ws1.row_dimensions[r].height = 180
                    id = id + 1
                    r = r + 1

    def testCaseMobileJSON(self,req_data,workbook):
        border = Border(left=Side(border_style='thin',
                         color='FF000000'),
                 right=Side(border_style='thin',
                            color='FF000000'),
                 top=Side(border_style='thin',
                          color='FF000000'),
                 bottom=Side(border_style='thin',
                             color='FF000000'),
                )

        e = 'To Verify Adobe variables match those detailed in the JSON. \n \n Pre Condition: Charles Proxy tool to be launched for testing purpose.'
        g = 'Ensure Charles Proxy is active'

        note = 'Please note: All native requests are POST requests \n Check Request Headers in Charles Proxy'
        developement = 'Dev '
        production = 'Prod '
        message='environment: All requests are for "POST /b/ss/cibcnativeappdev/0/'
        code='xxxxxx'

        ws1 = workbook.create_sheet("JSON Test Case",3)
        ws1.row_dimensions[1].height = 24
        ws1.row_dimensions[2].height = 63.6

        # set the width of column in Mobile JSON Test Sheet
        ws1.column_dimensions['B'].width = 10
        ws1.column_dimensions['D'].width = 30
        ws1.column_dimensions['F'].width = 30
        ws1.column_dimensions['E'].width = 14.89
        ws1.column_dimensions['G'].width = 25
        ws1.column_dimensions['H'].width = 120

        #Column Header in Mobile JSON Test Case Sheet
        ws1.cell(row = 1 , column= 1).value = 'Sr. No.'

        ws1.cell(row = 1 , column= 2).value = 'Date Created'
        ws1.cell(row = 1 , column= 3).value = 'Subject'
        ws1.cell(row = 1 , column= 4).value = 'Test Case Name'
        ws1.cell(row = 1 , column= 5).value = 'Test Objective'
        ws1.cell(row = 1 , column= 6).value = 'Step Name'
        ws1.cell(row = 1 , column= 7).value = 'Description'
        ws1.cell(row = 1 , column= 8).value = 'Expected Result'
        ws1.cell(row = 1 , column= 9).value = 'Author'

        for i in range(1,10):
             ws1.cell(row = 1 , column= i).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
             ws1.cell(row = 1 , column= i).font = Font(bold=True,color='008000')
             ws1.cell(row = 1 , column= i).border = border

        ws1.cell(row = 2, column= 1).value = note + '\n \t'+developement+message+code+'\n \t'+production+message+code
        ws1.cell(row = 2 , column= 1).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
        ws1.cell(row = 2 , column= 1).font = Font(color='008000')
        ws1.cell(row = 2 , column= 1).border = border

        ws1.merge_cells('A2:G2')
        ws1.merge_cells('H2:Z2')

        id = 1
        r = 3
        c = 1
        now = date.today()
        full = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

        for i in range(0, len(req_data['pages'])):
            event = 'Events: '
            comment = ' //'
            ws1.row_dimensions[r].height = 203.6
            if 'page_name' in req_data['pages'][i]:
                ws1.cell(row=r, column=c).value = str(id)
                ws1.cell(row = r , column= c).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c).border = border

                ws1.cell(row=r, column=c + 1).value = full
                ws1.cell(row=r, column=c + 1).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row = r , column= c + 1).border = border

                ws1.cell(row=r, column=c + 2).value = req_data['project_name']
                ws1.cell(row=r, column=c + 2).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 2).border = border

                ws1.cell(row=r, column=c + 4).value = e
                ws1.cell(row=r, column=c + 4).alignment = openpyxl.styles.Alignment(horizontal='left', vertical='center', wrap_text=True)
                ws1.cell(row = r , column= c + 4).border = border

                ws1.cell(row=r, column=c + 6).value = g
                ws1.cell(row=r, column=c + 6).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row = r , column= c + 6).border = border

                val = req_data['pages'][i]['page_name']
                b = '-.'
                for char in b:
                    val = val.replace(char, " ")
                ws1.cell(row=r, column=c + 3).value = val.title()
                ws1.cell(row=r, column=c + 5).value = req_data['pages'][i]['page_name']

                ws1.cell(row=r, column=c + 3).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 3).border = border
                ws1.cell(row=r, column=c + 5).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center', wrap_text=True)
                ws1.cell(row=r, column=c + 5).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 5).border = border
            if 'site_brand' in req_data:
                dct = 'page_name: ' + str(
                    req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                    req_data['pages'][i]['page_name']) + '  //Unique for each Page' + '\n '+'Site.name : ' + str(
                    req_data['site_name']) + '  //Name of the Site \n Site.type : ' + str(req_data['site_type']) + '  //Type of the Site' + '\n page.url:' + str(
                    req_data['pages'][i]['page_url']) + '  // URL of the Page' + '\n page.referrer: ' + str(
                    req_data['pages'][i]['page_referrer']) + '  //Previous Page Name' + '\n page.hierarchy: ' + str(
                    req_data['pages'][i]['page_hierarchy']) + ' // Hierarchy of the Page' + '\n page.language: ' + str(
                    req_data['pages'][i]['page_language']) + '    // Language Supported For Page' + '\n page.accessibilty: ' + str(
                    req_data['pages'][i]['page_accessibility']) + ' //Page Accessibility \n user.Authstate:' + str(
                    req_data['pages'][i]['user_auth_state']) + ' // depending on pre sign on or post sign on \n user.Type: ' + str(
                    req_data['pages'][i]['user_type'])+ ' //Type of the User \n user.ID: ' + '' + str(
                    req_data['pages'][i]['user_id']) + '   //user Id for the post sign on. it should be consistent throughout the whole app. ' + '\n \n'
                ws1.cell(row=r, column=c + 7).value = str(dct)
                ws1.cell(row=r, column=c + 7).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                ws1.cell(row = r , column= c + 7).border = border

                ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c + 8).border = border
                ws1.row_dimensions[r].height = 180
            id = id + 1
            r = r + 1
        for i in range(0, len(req_data['interaction'])):
            #ws1.row_dimensions[r].height = 203.6
            if 'page_name' in req_data['interaction'][i]:

                ws1.cell(row=r, column=c).value = str(id)
                ws1.cell(row = r , column= c ).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c + 2).border = border

                ws1.cell(row=r, column=c + 1).value = full
                ws1.cell(row = r , column= c+ 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c + 1).border = border

                ws1.cell(row=r, column=c + 2).value = req_data['project_name']
                ws1.cell(row = r , column= c + 2).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 2).border = border
                
                ws1.cell(row=r, column=c + 4).value = e
                ws1.cell(row = r , column= c+4).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                ws1.cell(row = r , column= c + 4).border = border

                ws1.cell(row=r, column=c +6).value = g
                ws1.cell(row = r , column= c+6).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c + 6).border = border

                val = req_data['interaction'][i]['interaction_name']
                b = '-.'
                for char in b:
                    val = val.replace(char, " ")
                ws1.cell(row=r, column=c + 3).value = val.title()
                ws1.cell(row = r , column= c+3).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 3).border = border

                ws1.cell(row=r, column=c + 5).value = req_data['interaction'][i]['interaction_name']
                ws1.cell(row = r , column= c+5).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row=r, column=c + 5).font = openpyxl.styles.Font(bold=True)
                ws1.cell(row = r , column= c + 5).border = border

            if 'site_brand' in req_data:
                dct = 'page_name' + str(
                    req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                    req_data['interaction'][i]['page_name']) + '    //Unique for each Page {Interaction Page}' + '\n'+ 'site.name :' + str(
                    req_data['site_name']) + ' //Name of the Site\n site.type:' + str(req_data['site_type']) + '  //Type of the site' + '\n page.url: ' + str(
                    req_data['interaction'][i]['page_url']) + '//URL of the Page' + '\n page.referreer:' + str(
                    req_data['interaction'][i]['page_referrer']) + '//Previous Page Name' + '\n page.hierarchy:' + str(
                    req_data['interaction'][i]['page_hierarchy']) + '  // Hierarchy of the Page' + '\n page.language: ' + str(
                    req_data['interaction'][i][
                        'page_language']) + '    // Language Supported For Page' + '\n page.accessibility:' + str(
                    req_data['interaction'][i]['page_accessibility']) + '//Page Accessibility ' + '\n interaction.name: ' + str(
                    req_data['interaction'][i]['interaction_name']) + " //Interaction Name \n event.siteInteraction: " + req_data['interaction'][i]['site_interaction_event'] + '// Site Interaction Event '
                ws1.cell(row=r, column=c + 7).value = str(dct)
                ws1.cell(row = r , column= c + 7).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                ws1.cell(row = r , column= c + 7).border = border

                ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                ws1.cell(row = r , column= c + 8).border = border

                ws1.row_dimensions[r].height = 203
            id = id + 1
            r = r + 1
        for parent in range(0, len(req_data['forms'])):
            for child in range(0, len(req_data['forms'][parent]['steps'])):
                if 'page_name' in req_data['forms'][parent]['steps'][child]:
                    ws1.cell(row=r, column=c).value = req_data['forms'][parent]['steps'][child]['page_name']
                    ws1.cell(row = r , column= c).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row=r, column=1).value = str(id)
                    ws1.cell(row = r , column= 1).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row = r , column= 1).border = border

                    ws1.cell(row=r, column=2).value = full
                    ws1.cell(row = r , column= 2).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row=r, column=c + 2).font = openpyxl.styles.Font(bold=True)
                    ws1.cell(row = r , column= c + 2).border = border

                    ws1.cell(row=r, column=3).value = req_data['project_name']
                    ws1.cell(row = r , column= 3).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row=r, column=c + 3).font = openpyxl.styles.Font(bold=True)
                    ws1.cell(row = r , column= c + 3).border = border

                    ws1.cell(row=r, column=5).value = e
                    ws1.cell(row = r , column= 5).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                    ws1.cell(row=r, column=c + 5).font = openpyxl.styles.Font(bold=True)
                    ws1.cell(row = r , column= c + 5).border = border

                    ws1.cell(row=r, column=7).value = g
                    ws1.cell(row = r , column= 7).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row = r , column= c + 7).border = border

                    val = req_data['forms'][parent]['steps'][child]['page_name']
                    b = '-.'
                    for char in b:
                        val = val.replace(char, " ")

                    ws1.cell(row=r, column=4).value = val.title()
                    ws1.cell(row = r , column= 4).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row = r , column= c + 4).border = border

                    ws1.cell(row=r, column=6).value = val.title()
                    ws1.cell(row = r , column= 6).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row = r , column= c + 6).border = border

                    dt = 'page_name:' + str(
                        req_data['site_brand']) + '>' + str(req_data['site_name']) + '>' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_name']) + ' //Unique for each Page \n '+ 'site.name:' + str(
                        req_data['site_name']) + ' //Site Name \n site.type:' + str(req_data[
                                                              'site_type']) + '    //Type of the Site' + '\n page.url: ' + str(
                        req_data['forms'][parent]['steps'][child]['page_url']) + '  //URL of the Page' + '\n page.referrer: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_referrer']) + ' //Previous Page Name' + '\n page.hierarchy' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_hierarchy']) + ' // Hierarchy of the Page' + '\n page.language: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'page_language']) + '// Language Supported For Page' + '\n page.accessibility: ' + str(
                        req_data['forms'][parent]['steps'][child]['page_accessibility']) + '//Page Accessibility \n user.Authstate:' + str(
                        req_data['forms'][parent]['steps'][child]['user_auth_state']) + '// depending on pre sign on or post sign on \n user.Type' + str(
                        req_data['forms'][parent]['steps'][child][
                            'user_type']) + '}' + ' //Type of the User \n user.ID: ' + '' + str(
                        req_data['forms'][parent]['steps'][child]['user_id']) + ' //user Id for the post sign on. it should be consistent throughout the whole app. ' + '\n form.name: ' + str(
                        req_data['forms'][parent]['form_name']) + ' // Form Name' + '\n step.name: ' + str(
                        req_data['forms'][parent]['steps'][child][
                            'step_name']) + ' //Form Step Name' + ' \n unique.id: ' + str(
                        req_data['forms'][parent]['steps'][child]['unique_id']) + ' // Unique Id of Form'
                    if req_data['forms'][parent]['is_transaction_exist'] == 'true':
                        dt = dt + '\n transaction.from: ' + str(
                            req_data['forms'][parent]['steps'][child]['from_transaction']) + '// Transaction From \n transaction.to: ' + str(
                            req_data['forms'][parent]['steps'][child][
                                'to_transaction']) + ' //To Transaction'
                    if req_data['forms'][parent]['is_product_exist'] == 'true':
                        dt = dt + '\n positioning: ' + str(req_data['forms'][parent]['steps'][child][
                                                          'product_positioning']) + '// Product Positioning\n grouping: ' + str(
                            req_data['forms'][parent]['steps'][child][
                                'product_grouping']) + '    //Product grouping \n parent_product: ' + str(
                            req_data['forms'][parent]['steps'][child][
                                'parent_product']) + ' // Parent Product \nadjudication:' + str(
                            req_data['forms'][parent]['steps'][child]['adjudication']) + '   // Adjudication\n '


                    ws1.cell(row=r, column=c + 7).value = str(dt)
                    ws1.cell(row = r , column= c + 7).alignment = openpyxl.styles.Alignment(horizontal='left',vertical='top',wrapText=True)
                    ws1.cell(row = r , column= c + 7).border = border

                    ws1.cell(row=r, column=c + 8).value = req_data['user_name']
                    ws1.cell(row = r , column= c + 8).alignment = openpyxl.styles.Alignment(horizontal='center',vertical='center',wrapText=True)
                    ws1.cell(row = r , column= c + 8).border = border

                    ws1.row_dimensions[r].height = 203
                    id = id + 1
                    r = r + 1
