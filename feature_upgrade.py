# ==============================================================================
# CASE STUDY: CODE REFRACTORING & FEATURE ADDITION DEMO
# Demonstrating how I transform fragile code into robust, production-ready systems.
# ==============================================================================

# ------------------------------------------------------------------------------
# ❌ [STAGE 1: THE BUGGY LEGACY CODE]
# Submitted by Client: This version crashes easily on invalid inputs and 
# doesn't persist any historical logs or data.
# ------------------------------------------------------------------------------
"""
def process_user_data_OLD(name, score):
    # CRASH RISK: Will raise ValueError if score is a formatted string (e.g., "85%")
    if float(score) >= 50:
        return f"{name} Passed"
    else:
        return f"{name} Failed"
"""


# ------------------------------------------------------------------------------
#  [STAGE 2: THE CLEAN & FIXED CODE]
# My Solution: Added Type Hinting, Robust Exception Handling, and a Data Logging Feature.
# ------------------------------------------------------------------------------
def process_user_data(name: str, score: float | str) -> str:
    """Processes student score data, determines pass/fail status,
    and appends the records securely to an external text file.
    """
    try:
        # Secure string cleaning and type conversion
        if isinstance(score, str):
            score_cleaned = score.replace("%", "").strip()
        else:
            score_cleaned = score

        score_num = float(score_cleaned)
        status = "Passed" if score_num >= 50 else "Failed"
        
        output_line = f"Student: {name} | Score: {score_num} | Status: {status}\n"
        
        # [NEW INTEGRATED FEATURE]: Automated File Logging
        # Appends data to a local text file to preserve historical logs safely
        with open("student_records.txt", "a", encoding="utf-8") as file:
            file.write(output_line)
            
        return f"✔ Modified function executed successfully! Data saved for {name}. Status: {status}"
        
    except ValueError:
        return f"❌ Error: Invalid score value '{score}' provided. Cannot convert to float."
    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"


if __name__ == "__main__":
    print("====================================")
    print("   FEATURE ADDITION SYSTEM DEMO     ")
    print("====================================")
    
    # Simulating robust student data processing and automated logging
    print(process_user_data("Ali", 85))
    print(process_user_data("Sara", "42%"))  # Handles strings smoothly now!
    print(process_user_data("Youssef", 90))
    
    print("\n✔ [Check your local directory for 'student_records.txt' to view the generated logs]")
    
  
