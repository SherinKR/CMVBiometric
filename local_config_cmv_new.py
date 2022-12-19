
# ERPNext related configs
ERPNEXT_API_KEY = '5a914d2f30589a9'
ERPNEXT_API_SECRET = 'd38ce06318c6bdf'
ERPNEXT_URL = 'https://cmverp-dev.frappe.cloud'


# operational configs
PULL_FREQUENCY = 1 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = '20220901' # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
                                    #(Caution: this feature can lead to data loss if used carelessly.)
    #{'device_id':'CEXJ204760487','ip':'192.168.1.81', 'punch_direction':'AUTO', 'clear_from_device_on_fetch': False},
devices = [
    {'device_id':'BRM9213360010','ip':'192.168.1.82', 'punch_direction':'AUTO', 'clear_from_device_on_fetch': False},
    {'device_id':'BRM9183860084','ip':'192.168.1.84', 'punch_direction':'AUTO', 'clear_from_device_on_fetch': False},
    {'device_id':'BRM9213960074','ip':'192.168.1.96', 'punch_direction':'AUTO', 'clear_from_device_on_fetch': False},
    {'device_id':'BRM9203460113','ip':'192.168.1.87', 'punch_direction':'AUTO', 'clear_from_device_on_fetch': False},    
]

# Configs updating sync timestamp in the Shift Type DocType 
# please, read this thread to know why this is necessary https://discuss.erpnext.com/t/v-12-hr-auto-attendance-purpose-of-last-sync-of-checkin-in-shift-type/52997
shift_type_device_mapping = [
    {'shift_type_name': ['SCAVENGER - House Keeping', 'STORE OPERATOR - Worker', 'FINISHING ASSISTANT - Worker', 'HR EXECUTIVE - Production Staff', 'COOKING MASTER - Cook', 'FABRIC EXECUTIVE - Production Staff', 'TECHNICIAN - Production Staff', 'SENIOR MERCHANDISER - Admin', 'MERCHANDISER - Admin', 'MERCHANDISER QA - Admin', 'JUNIOR MERCHANDISER - Admin','LOGISTIC INCHARGE - Admin', 'LOGISTIC EXECUTIVE - Admin', 'WARDEN - Warden', 'SECURITY GUARD - Night Security', 'SECURITY GUARD - Day Security', 'NURSE', 'House Keeping', 'COOK HELPER - Cook', 'TRAINING INCHARGE - Production Staff', 'TRAINER - Production Staff', 'STORE INCHARGE - Production Staff', 'PURCHASE MANAGER - Production Staff', 'STORE SUPERVISOR - Production Staff', 'SAMPLE TECHNICIAN - Production Staff', 'SAMPLE INCHARGE - Production Staff', 'PRE PRODUCTION MANAGER - Production Staff', 'QAD PRESENTATION - Production Staff', 'Q.C - Production Staff', 'Q.A.D MANAGER - Production Staff', 'Q.A - Production Staff', 'FABRIC QC - Production Staff', 'CUTTING QC - Production Staff', 'AQL AUDITOR - Production Staff', 'SR.TECHNICIAN - Production Staff', 'PRODUCTION-CO-ORDINATOR - Production Staff', 'PRODUCTION INCHARGE - Production Staff', 'LOADING SUPERVISOR - Production Staff', 'LINE SUPERVISOR - Production Staff', 'LINE GUIDE - Production Staff', 'FACTORY MANAGER - Production Staff', 'A.P.M - Production Staff', 'PLANNING ASSISTANT - Production Staff', 'MECHANIC INCHARGE - Production Staff', 'MECHANIC - Production Staff', 'LAB INCHARGE - Production Staff', 'I E - Production Staff', 'I.E iNCHARGE - Production Staff', 'JR.HR EXECUTIVE - Production Staff', 'HR MANAGER - Production Staff', 'DRIVER - Production Staff' , 'DEPUTY GENERAL MANAGER - Production Staff', 'PICKING SUPERVISOR - Production Staff' , 'FINISHING INCHARGE - Production Staff', 'FINISHING INCHARGE - Production Staff', 'TRAINEE - Worker', 'STORE HELPER - Worker', 'LABEL OPERATOR - Worker', 'OPERATOR - Worker', 'BUTTON OPERATOR - Worker', 'QC TRAINEE - Worker', 'CHECKER - Worker', 'TRIMMING - Worker', 'TEMPLATE MACHINE OPERATOR - Worker', 'STAIN REMOVER - Worker', 'PRODUCTION HELPER - Worker', 'LOADING HELPER - Worker', 'BUTTONING HELPER - Worker', 'MAINTENANCE TRAINEE - Worker', 'PICKING - Worker', 'PACKER - Worker', 'IRONER - Worker', 'FINISHING SUPERVISOR - Worker', 'AIRPORT PACKER - Worker', 'FABRIC INCHARGE - Production Staff', 'FABRIC HELPER - Production Staff', 'FABRIC CO-ORDINATOR - Production Staff', 'DATA ENTRY - Production Staff', 'MAINTENANCE INCHARGE - Production Staff', 'ELECTRICIAN - Production Staff', 'EDP-INCHARGE - Admin', 'EDP EXECUTIVE - Admin', 'EDP ASSISTANT - Admin', 'STICKERING HELPER - Worker', 'SPREADER OPERATOR - Worker', 'SPREADER HELPER - Worker', 'FUSING HELPER - Worker', 'CUTTING HELPER - Worker', 'CUTTING SUPERVISOR - Production Staff', 'CUTTING MASTER - Worker', 'CAD INCHARGE - Production Staff', 'CAD ASSISTANT - Production Staff', 'ACCOUNTS ASSISTANT - Admin', 'ACCOUNTANT - Admin', 'SENIOR ACCOUNTANT - Admin', 'ICAD EXECUTIVE -Admin'], 'related_device_id': ['BRM9213360010', 'CEXJ204760487', 'BRM9183860084', 'BRM9213960074', 'BRM9203460113']}
]


# Ignore following exceptions thrown by ERPNext and continue importing punch logs.
# Note: All other exceptions will halt the punch log import to erpnext.
#       1. No Employee found for the given employee User ID in the Biometric device.
#       2. Employee is inactive for the given employee User ID in the Biometric device.
#       3. Duplicate Employee Checkin found. (This exception can happen if you have cleared the logs/status.json of this script)
# Use the corresponding number to ignore the above exceptions. (Default: Ignores all the listed exceptions)
allowed_exceptions = [1,2,3]
