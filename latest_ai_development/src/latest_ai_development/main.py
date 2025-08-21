#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Ensure reports directory exists
    os.makedirs('reports', exist_ok=True)
    
    inputs = {
        'topic': 'Open Source Secure MCP Servers',
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = LatestAiDevelopment().crew().kickoff(inputs=inputs)
        # Check if result was successful (has content)
        if result and hasattr(result, 'raw') and result.raw:
            print(f"\n✅ Crew execution completed successfully!")
            print(f"📄 Report saved to timestamped file in reports/ directory")
            return result
        elif result:
            print(f"\n✅ Crew execution completed successfully!")
            print(f"📄 Report saved to timestamped file in reports/ directory")
            return result
        else:
            print(f"\n⚠️ Crew execution completed but no result was returned")
            return None
    except Exception as e:
        # Log the actual exception for debugging
        print(f"\n❌ An error occurred while running the crew: {e}")
        print(f"🔍 Exception type: {type(e).__name__}")
        print(f"🔍 Check the error details above for troubleshooting")
        # Re-raise the original exception to preserve stack trace
        raise


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        LatestAiDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        LatestAiDevelopment().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
