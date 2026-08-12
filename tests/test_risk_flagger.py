from integrity_detection.risk_flagger import (
    generate_risk_flag,
    generate_alert_message
)


print("=" * 50)
print("INTEGRITY RISK FLAGGING")
print("=" * 50)


print("\nHIGH RISK")

print(generate_risk_flag(85))
print(generate_alert_message(85))


print("\nMEDIUM RISK")

print(generate_risk_flag(55))
print(generate_alert_message(55))


print("\nLOW RISK")

print(generate_risk_flag(20))
print(generate_alert_message(20))