"""
Weyou Backend Challenge - Fix the Broken API
When fixed correctly, running this will reveal your answer code.
"""

import json
from datetime import datetime

# BUG: Typo in constant name
SECRET_ANSER_CODE = "WBK2025BE"


class CaseAnalyzer:
    """Analyzes legal case complexity"""
    
    def __init__(self):
        self.case_types = {
            "civil": 30,
            "criminal": 60,
            "corporate": 45
        }
    
    def calculate_complexity(self, case_type, num_documents):
        """Calculate case complexity score"""
        if case_type not in self.case_types:
            return None
        
        base_score = self.case_types[case_type]
        # BUG: Wrong operator (+ instead of *)
        doc_score = num_documents + 2
        
        return base_score + doc_score
    
    def get_recommendation(self, complexity):
        """Get recommendation based on complexity"""
        if complexity < 50:
            return "Low complexity - Single lawyer recommended"
        elif complexity < 80:
            return "Medium complexity - Team of 2-3 lawyers recommended"
        else:
            return "High complexity - Full legal team required"


# BUG: Missing colon
def generate_report(case_type, num_documents)
    """Generate analysis report"""
    analyzer = CaseAnalyzer()
    
    # BUG: Missing argument
    complexity = analyzer.calculate_complexity(case_type)
    
    if complexity is None:
        return {"error": "Invalid case type"}
    
    recommendation = analyzer.get_recommendation(complexity)
    
    report = {
        "case_type": case_type,
        "documents": num_documents,
        "complexity_score": complexity,
        "recommendation": recommendation,
        "timestamp": datetime.now().isoformat()
    }
    
    return report


def unlock_answer_code():
    """Unlock the answer code if everything works"""
    print("\n" + "="*60)
    print("🎉 CONGRATULATIONS! YOU FIXED ALL THE BUGS!")
    print("="*60)
    print("\nRunning test cases...\n")
    
    # Test Case 1
    report1 = generate_report("civil", 10)
    print(f"✅ Test 1 Passed: {report1['recommendation']}")
    
    # Test Case 2
    report2 = generate_report("criminal", 25)
    print(f"✅ Test 2 Passed: {report2['recommendation']}")
    
    # Test Case 3
    report3 = generate_report("corporate", 15)
    print(f"✅ Test 3 Passed: {report3['recommendation']}")
    
    print("\n" + "="*60)
    print("🔓 YOUR ANSWER CODE:")
    print("="*60)
    # BUG: Wrong variable name
    print(f"\n    {SECRET_ANSER_CODE}\n")
    print("="*60)
    print("\n📤 Submit this code on the website!\n")


if __name__ == "__main__":
    try:
        unlock_answer_code()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Hint: There are still bugs to fix!")
        print("Debug the code and try again.\n")

