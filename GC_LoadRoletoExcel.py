import xlsxwriter, sys


def loadExcel(response_json):
    permissionPoliciesLen = len(response_json["entities"][0]["permissionPolicies"])
    k=0
    wb = xlsxwriter.Workbook(f"Role_{sys.argv[1]}.xlsx")
    ws = wb.add_worksheet(f"Permission_{sys.argv[1]}")
    for i in range(permissionPoliciesLen):
        actionSetLen = len(response_json["entities"][0]["permissionPolicies"][i]["actionSet"])
        for j in range (actionSetLen):
            domain = response_json["entities"][0]["permissionPolicies"][i]["domain"]
            entityName = response_json["entities"][0]["permissionPolicies"][i]["entityName"]
            actionSet = response_json["entities"][0]["permissionPolicies"][i]["actionSet"][j]
            if actionSet == "*":
                actionSet = "ALL"
            if entityName == "*":
                entityName = "ALL"
            permission = domain+" > "+entityName+" > "+actionSet
            ws.write(k,0,permission)
            k=k+1
    wb.close()