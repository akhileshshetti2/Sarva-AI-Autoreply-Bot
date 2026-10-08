import time
import pyautogui
import pyperclip
from ai_engine import ask_sarva

# Enable PyAutoGUI safety fail-safe:
# Moving your mouse cursor to any corner of the screen will force-stop the script.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def get_message():
    """Extracts and returns the full chat history from WhatsApp."""
    # Step 1: Focus WhatsApp from taskbar
    pyautogui.click(x=1265, y=1046)
    time.sleep(0.5)

    # Step 2: Click start coordinate of chat area
    pyautogui.click(x=551, y=184)
    time.sleep(0.5)

    # Step 3: Shift + Click at end coordinate to select chat history
    pyautogui.keyDown('shift')
    pyautogui.click(x=1865, y=906)
    pyautogui.keyUp('shift')
    time.sleep(0.5)

    # Step 4: Copy to clipboard and un-highlight
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click()
    time.sleep(0.5)

    # Step 5: Return extracted text
    return pyperclip.paste()


def send_reply(reply_text: str):
    """Pastes and sends the AI reply into WhatsApp."""
    pyperclip.copy(reply_text)

    # Click inside WhatsApp text field
    pyautogui.click(x=625, y=977)
    time.sleep(0.5)

    # Paste text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    # Send using ENTER
    pyautogui.press('enter')


if __name__ == "__main__":
    print("=== WhatsApp Auto Reply Bot Started ===")
    print("Press Ctrl+C in terminal or move mouse to screen corner to stop.\n")

    # Keep track of the last processed message to avoid replying to the same message twice
    last_processed_message = ""

    while True:
        try:
            # Step 1: Read current chat history
            history = get_message()
            cleaned_history = history.strip()

            # Separate into individual lines
            lines = [line.strip() for line in cleaned_history.split('\n') if line.strip()]

            if lines:
                latest_line = lines[-1]

                # Condition 1: Check if Akhil sent the last message
                if "Akhil:" in latest_line:
                    print("[Monitoring] Last message is from Akhil. Waiting for new incoming messages...")
                
                # Condition 2: Check if this message was already responded to
                elif latest_line == last_processed_message:
                    print("[Monitoring] No new incoming messages. Waiting...")

                # Condition 3: A NEW message from the other person has arrived!
                else:
                    print(f"\n[NEW MESSAGE DETECTED] -> {latest_line}")
                    print("Generating AI reply...")

                    ai_reply = ask_sarva(history)

                    if ai_reply and ai_reply.strip():
                        print(f"Replying: {ai_reply}")
                        send_reply(ai_reply)

                        # Update state so we don't reply to this exact line again
                        last_processed_message = latest_line
                    else:
                        print("[INFO] AI returned an empty response.")

            # Wait 5 seconds before checking WhatsApp again
            time.sleep(5)

        except Exception as e:
            print(f"[ERROR] An issue occurred: {e}")
            time.sleep(5)