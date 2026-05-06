import os
import pandas as pd
import matplotlib.pyplot as plt

# ===== 1. ЧИТАЕМ СЕКРЕТНЫЕ КЛЮЧИ =====
RISK_THRESHOLD = float(os.getenv("ACCESS_RISK_THRESHOLD", 0.6))
AUDIT_TOKEN = os.getenv("NETWORK_AUDIT_TOKEN", "default")
DEVICE_SECRET = os.getenv("PHYSICAL_DEVICE_SECRET", "default")

print("=" * 50)
print("КОНТЕЙНЕР БЕЗОПАСНОСТИ (ВАРИАНТ 31)")
print("=" * 50)
print(f"Порог риска (из секрета): {RISK_THRESHOLD}")
print(f"Токен аудита: {AUDIT_TOKEN[:4] if AUDIT_TOKEN != 'default' else 'None'}***")
print(f"Секрет устройства: {DEVICE_SECRET[:4] if DEVICE_SECRET != 'default' else 'None'}***")
print()

# ===== 2. БАЗА ЗНАНИЙ =====
device_criticality = {
    "switch": {"core": 0.9, "access": 0.5},
    "router": {"core": 0.95, "edge": 0.7},
    "patch_panel": {"main": 0.4, "aux": 0.3}
}

role_risk_factor = {
    "admin": 0.3,
    "user": 0.6,
    "guest": 0.9
}

# ===== 3. ФУНКЦИЯ РАСЧЁТА РИСКА (КОНТЕЙНЕР РАСЧЁТА) =====
def calculate_risk(device_type, device_subtype, role):
    if device_type not in device_criticality:
        return 1.0
    crit = device_criticality[device_type].get(device_subtype, 0.5)
    role_factor = role_risk_factor.get(role, 0.8)
    return round(crit * role_factor, 3)

# ===== 4. ТЕСТОВЫЕ ЗАПРОСЫ (ИМИТАЦИЯ ОБРАЩЕНИЙ К ОБОРУДОВАНИЮ) =====
requests = [
    {"id": 1, "device_type": "switch", "subtype": "core", "role": "guest"},
    {"id": 2, "device_type": "router", "subtype": "core", "role": "admin"},
    {"id": 3, "device_type": "patch_panel", "subtype": "main", "role": "user"},
    {"id": 4, "device_type": "switch", "subtype": "access", "role": "admin"},
    {"id": 5, "device_type": "router", "subtype": "edge", "role": "guest"},
    {"id": 6, "device_type": "firewall", "subtype": "unknown", "role": "user"}
]

# ===== 5. ОБРАБОТКА ЗАПРОСОВ =====
results = []

print("ОБРАБОТКА ЗАПРОСОВ К ФИЗИЧЕСКОМУ ОБОРУДОВАНИЮ")
print("-" * 50)

for req in requests:
    risk = calculate_risk(req["device_type"], req["subtype"], req["role"])
    decision = "ALLOW" if risk <= RISK_THRESHOLD else "DENY"

    results.append({
        "id": req["id"],
        "device": f"{req['device_type']}/{req['subtype']}",
        "role": req["role"],
        "risk": risk,
        "decision": decision
    })

    print(f"Запрос {req['id']}: {req['device_type']}/{req['subtype']} | Роль: {req['role']} | Риск: {risk} | Решение: {decision}")

print()
print(f"Статистика: ALLOW = {sum(1 for r in results if r['decision'] == 'ALLOW')}, DENY = {sum(1 for r in results if r['decision'] == 'DENY')}")
print()

# ===== 6. КОНТЕЙНЕР ТАБЛИЧНОГО ПРЕДСТАВЛЕНИЯ =====
df = pd.DataFrame(results)
print("ТАБЛИЦА РЕШЕНИЙ")
print("=" * 50)
print(df.to_string(index=False))
print()

# Сохраняем в CSV
df.to_csv("security_audit.csv", index=False)
print("Сохранено: security_audit.csv")

# ===== 7. КОНТЕЙНЕР ВИЗУАЛИЗАЦИИ =====
allowed = sum(1 for r in results if r["decision"] == "ALLOW")
denied = len(results) - allowed

# График 1: столбчатая диаграмма
plt.figure(figsize=(6, 4))
plt.bar(["Разрешено (ALLOW)", "Заблокировано (DENY)"], [allowed, denied], color=["green", "red"])
plt.title("Решения контейнера безопасности")
plt.ylabel("Количество запросов")
plt.savefig("security_decisions.png")
plt.close()
print("Сохранено: security_decisions.png")

# График 2: линейный график рисков
ids = [r["id"] for r in results]
risks = [r["risk"] for r in results]

plt.figure(figsize=(8, 4))
plt.plot(ids, risks, marker="o", linestyle="--", color="blue", linewidth=2)
plt.axhline(y=RISK_THRESHOLD, color="red", linestyle=":", label=f"Порог риска ({RISK_THRESHOLD})")
plt.xlabel("ID запроса")
plt.ylabel("Уровень риска")
plt.title("Динамика рисков запросов к оборудованию")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("risk_trend.png")
plt.close()
print("Сохранено: risk_trend.png")

print("\n" + "=" * 50)
print("РАБОТА ВСЕХ КОНТЕЙНЕРОВ ЗАВЕРШЕНА")
print("=" * 50)