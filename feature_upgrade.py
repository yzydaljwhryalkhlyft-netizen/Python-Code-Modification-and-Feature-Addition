# --------------------------------------------------
# Period 3: Code Modification & Feature Addition Demo
# --------------------------------------------------

def process_user_data(name: str, score: float | str) -> str:
    """Processes student score data, determines pass/fail status,

    and appends the records to an external text file.
    """
    try:
        # Determine performance status based on the score threshold
        score_num = float(score)
        status = "Passed" if score_num >= 50 else "Failed"
        
        output_line = f"Student: {name} | Score: {score_num} | Status: {status}\n"
        
        # [NEW FEATURE]: Automated File Logging
        # Appends data to a local text file to preserve historical logs
        with open("student_records.txt", "a", encoding="utf-8") as file:
            file.write(output_line)
            
        return f"✔ Modified function executed successfully! Data saved for {name}. Status: {status}"
        
    except ValueError:
        return "❌ Error: Invalid score value provided."
    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"


if __name__ == "__main__":
    print("====================================")
    print("   FEATURE ADDITION SYSTEM DEMO     ")
    print("====================================")
    
    # Simulating student data processing and automated logging
    print(process_user_data("Ali", 85))
    print(process_user_data("Sara", 42))
    print(process_user_data("Youssef", 90))
    
    print("\n✔ [Check your local directory for 'student_records.txt' to view the generated logs]")
  
