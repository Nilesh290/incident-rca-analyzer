from datetime import datetime

print("======================================")
print("       INCIDENT RCA ANALYZER")
print("======================================")

incident_id = input("Enter Incident ID: ")
application = input("Enter Application Name: ")
error = input("Enter Error Message: ")
status_code = int(input("Enter HTTP Status Code: "))
response_time = float(input("Enter Response Time (seconds): "))
impact = input("Enter Business Impact: ")
resolution = input("Enter Resolution: ")

print("\n========== INCIDENT REPORT ==========")

print("Incident ID      :", incident_id)
print("Application      :", application)
print("Date & Time      :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Error            :", error)
print("HTTP Status      :", status_code)
print("Response Time    :", response_time, "seconds")
print("Business Impact  :", impact)
print("Resolution       :", resolution)

print("\n========== ANALYSIS ==========")

if status_code >= 500:
    print("Incident Type    : Server / Backend Error")
    print("Recommended RCA  : Check application logs, database and backend services.")

elif status_code >= 400:
    print("Incident Type    : Client / API Request Error")
    print("Recommended RCA  : Validate request parameters, authentication and API payload.")

elif response_time > 3:
    print("Incident Type    : Performance Issue")
    print("Recommended RCA  : Check database queries, API latency and server resources.")

else:
    print("Incident Type    : Normal")
    print("Recommended RCA  : No major technical issue detected.")

print("\n========== INCIDENT CLOSED ==========")
print("Status: Resolved")
