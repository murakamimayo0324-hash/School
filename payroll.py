def calculate_payroll(employees: list[dict]) -> list[dict]:
    """
    従業員リストの給与を計算する

    各従業員データ:
      - name: 氏名
      - hourly_rate: 時給（円）
      - hours_worked: 労働時間
      - overtime_hours: 残業時間（通常時間外）
    """
    OVERTIME_RATE = 1.25  # 残業割増率 (25%増)

    # 所得税率テーブル（簡易版）
    TAX_BRACKETS = [
        (1_950_000,  0.05),
        (3_300_000,  0.10),
        (6_950_000,  0.20),
        (9_000_000,  0.23),
        (18_000_000, 0.33),
        (40_000_000, 0.40),
        (float('inf'), 0.45),
    ]

    def calc_income_tax(annual_salary: float) -> float:
        """簡易所得税計算（累進課税）"""
        prev_limit = 0
        tax = 0.0
        for limit, rate in TAX_BRACKETS:
            if annual_salary <= prev_limit:
                break
            taxable = min(annual_salary, limit) - prev_limit
            tax += taxable * rate
            prev_limit = limit
        return tax / 12  # 月割り

    def calc_social_insurance(monthly_salary: float) -> float:
        """社会保険料（健康保険 + 厚生年金、概算）"""
        health = monthly_salary * 0.0500   # 健康保険 約5%
        pension = monthly_salary * 0.0915  # 厚生年金 約9.15%
        employment = monthly_salary * 0.003  # 雇用保険 約0.3%
        return health + pension + employment

    results = []
    for emp in employees:
        name = emp["name"]
        hourly_rate = emp["hourly_rate"]
        regular_hours = emp.get("hours_worked", 0)
        overtime_hours = emp.get("overtime_hours", 0)

        # 基本給 + 残業代
        regular_pay = hourly_rate * regular_hours
        overtime_pay = hourly_rate * OVERTIME_RATE * overtime_hours
        gross_pay = regular_pay + overtime_pay

        # 控除額
        social_insurance = calc_social_insurance(gross_pay)
        income_tax = calc_income_tax(gross_pay * 12)
        total_deductions = social_insurance + income_tax

        net_pay = gross_pay - total_deductions

        results.append({
            "name": name,
            "regular_pay": round(regular_pay),
            "overtime_pay": round(overtime_pay),
            "gross_pay": round(gross_pay),
            "social_insurance": round(social_insurance),
            "income_tax": round(income_tax),
            "total_deductions": round(total_deductions),
            "net_pay": round(net_pay),
        })

    return results


def print_payroll_report(results: list[dict]) -> None:
    """給与明細レポートを表示"""
    print("=" * 60)
    print(f"{'給与計算明細':^58}")
    print("=" * 60)

    for r in results:
        print(f"\n【{r['name']}】")
        print(f"  基本給          : {r['regular_pay']:>10,} 円")
        print(f"  残業代          : {r['overtime_pay']:>10,} 円")
        print(f"  ─────────────────────────────")
        print(f"  総支給額        : {r['gross_pay']:>10,} 円")
        print(f"  社会保険料      : {r['social_insurance']:>10,} 円")
        print(f"  所得税          : {r['income_tax']:>10,} 円")
        print(f"  控除合計        : {r['total_deductions']:>10,} 円")
        print(f"  ─────────────────────────────")
        print(f"  差引支給額(手取): {r['net_pay']:>10,} 円")

    print("\n" + "=" * 60)


# ── サンプルデータで実行 ──────────────────────────────────
if __name__ == "__main__":
    employees = [
        {"name": "田中 太郎", "hourly_rate": 2000, "hours_worked": 160, "overtime_hours": 20},
        {"name": "鈴木 花子", "hourly_rate": 1800, "hours_worked": 160, "overtime_hours": 0},
        {"name": "佐藤 次郎", "hourly_rate": 2500, "hours_worked": 140, "overtime_hours": 10},
    ]

    results = calculate_payroll(employees)
    print_payroll_report(results)
