from interview_summary.strengths_analyzer import analyze_strengths
from interview_summary.weakness_analyzer import analyze_weaknesses
from interview_summary.culture_analyzer import analyze_culture
from interview_summary.risk_detector import detect_risks
from interview_summary.inconsistency_detector import detect_inconsistencies
from interview_summary.performance_summary import summarize_performance


def generate_report(candidate):

    return {
        "candidate_name": candidate["name"],
        "strengths": analyze_strengths(candidate),
        "weaknesses": analyze_weaknesses(candidate),
        "cultural_fit": analyze_culture(candidate),
        "risk_flags": detect_risks(candidate),
        "inconsistencies": detect_inconsistencies(candidate),
        "overall_performance": summarize_performance(candidate)
    }