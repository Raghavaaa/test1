# Answer Key - Unlock Tests

## 🔑 Secret Answer Codes

### Frontend Test
**Answer Code:** `WFR2025FE`

**Magic Number:** 42

### Backend Test
**Answer Code:** `WBK2025BE`

---

## 🐛 Complete Bug List

### Frontend Test Bugs (6 total)

#### `broken_webpage.html`

1. **Line 27:** CSS property typo
   ```css
   dispaly: none;  ❌
   display: none;  ✅
   ```

2. **Line 50:** Button class typo
   ```html
   <button class="btn-submitt">  ❌
   <button class="btn-submit">   ✅
   ```

3. **Line 60:** JavaScript method name error
   ```javascript
   document.getElementByID("userInput")  ❌
   document.getElementById("userInput")  ✅
   ```

4. **Line 64:** Assignment instead of comparison
   ```javascript
   if (number = MAGIC_NUMBER) {  ❌
   if (number == MAGIC_NUMBER) { ✅
   // or use === for strict equality
   ```

5. **Hidden bug:** User needs to know magic number is 42
   - Hint given: "The answer to life, universe, and everything"
   - Reference to Hitchhiker's Guide to the Galaxy

### Backend Test Bugs (6 total)

#### `broken_api.py`

1. **Line 9:** Variable name typo
   ```python
   SECRET_ANSER_CODE = "WBK2025BE"  ❌
   SECRET_ANSWER_CODE = "WBK2025BE" ✅
   ```

2. **Line 30:** Wrong operator
   ```python
   doc_score = num_documents + 2  ❌
   doc_score = num_documents * 2  ✅
   ```

3. **Line 46:** Missing colon
   ```python
   def generate_report(case_type, num_documents)  ❌
   def generate_report(case_type, num_documents): ✅
   ```

4. **Line 51:** Missing argument
   ```python
   complexity = analyzer.calculate_complexity(case_type)        ❌
   complexity = analyzer.calculate_complexity(case_type, num_documents) ✅
   ```

5. **Line 83:** Wrong variable name (references bug #1)
   ```python
   print(f"\n    {SECRET_ANSER_CODE}\n")  ❌
   print(f"\n    {SECRET_ANSWER_CODE}\n") ✅
   ```

---

## ✅ Fixed Versions

### Frontend - Fixed Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weyou Frontend Challenge</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        #userInput {
            padding: 10px;
            width: 200px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 6px;
        }
        .btn-submit {
            padding: 12px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 20px;
        }
        .btn-submit:hover {
            background: #5568d3;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            background: #f0f0f0;
            border-radius: 8px;
            display: none;  /* FIXED */
        }
        .success {
            background: #d4edda !important;
            color: #155724;
            border: 2px solid #c3e6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Frontend Challenge</h1>
        <p>Enter the magic number between 1-100:</p>
        <input type="text" id="userInput" placeholder="Enter number">
        <button class="btn-submit" onclick="checkAnswer()">Submit</button>  <!-- FIXED -->
        <div id="result"></div>
    </div>

    <script>
        const MAGIC_NUMBER = 42;
        const SECRET_CODE = "WFR2025FE";

        function checkAnswer() {
            const input = document.getElementById("userInput").value;  // FIXED
            const number = parseInt(input);
            const resultDiv = document.getElementById("result");

            if (number === MAGIC_NUMBER) {  // FIXED
                resultDiv.style.display = "block";
                resultDiv.className = "success";
                resultDiv.innerHTML = `
                    <h2>🎉 Congratulations!</h2>
                    <p>You fixed all the bugs!</p>
                    <h3>Your Answer Code:</h3>
                    <h1 style="color: #667eea; font-size: 32px;">${SECRET_CODE}</h1>
                    <p style="font-size: 14px; color: #666;">Submit this code to complete the test</p>
                `;
            } else {
                resultDiv.style.display = "block";
                resultDiv.className = "";
                resultDiv.innerHTML = `<p>❌ Try again! Hint: The answer to life, universe, and everything...</p>`;
            }
        }
    </script>
</body>
</html>
```

### Backend - Fixed Code

```python
"""
Weyou Backend Challenge - Fix the Broken API
When fixed correctly, running this will reveal your answer code.
"""

import json
from datetime import datetime

SECRET_ANSWER_CODE = "WBK2025BE"  # FIXED


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
        doc_score = num_documents * 2  # FIXED
        
        return base_score + doc_score
    
    def get_recommendation(self, complexity):
        """Get recommendation based on complexity"""
        if complexity < 50:
            return "Low complexity - Single lawyer recommended"
        elif complexity < 80:
            return "Medium complexity - Team of 2-3 lawyers recommended"
        else:
            return "High complexity - Full legal team required"


def generate_report(case_type, num_documents):  # FIXED
    """Generate analysis report"""
    analyzer = CaseAnalyzer()
    
    complexity = analyzer.calculate_complexity(case_type, num_documents)  # FIXED
    
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
    print(f"\n    {SECRET_ANSWER_CODE}\n")  # FIXED
    print("="*60)
    print("\n📤 Submit this code to complete the challenge!\n")


if __name__ == "__main__":
    try:
        unlock_answer_code()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Hint: There are still bugs to fix!")
        print("Debug the code and try again.\n")
```

---

## 📊 Evaluation Criteria

### Frontend Test (100 points)
- CSS bug fixed: 15 points
- Button class fixed: 15 points
- getElementById fixed: 20 points
- Comparison operator fixed: 20 points
- Found magic number (42): 20 points
- Submitted correct code: 10 points

### Backend Test (100 points)
- Variable typo fixed: 15 points
- Operator fixed: 20 points
- Missing colon fixed: 15 points
- Missing argument fixed: 20 points
- Variable reference fixed: 20 points
- Submitted correct code: 10 points

---

## ✅ How to Verify Submissions

When candidates submit their answer codes:

**Frontend:** Should submit `WFR2025FE`  
**Backend:** Should submit `WBK2025BE`

If they submit these codes, they successfully:
1. Found all bugs
2. Fixed all bugs
3. Ran the program
4. Saw the success message

**Any other code = incomplete or incorrect**

---

**Keep this file confidential!** 🔒

