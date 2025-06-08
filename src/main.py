import time
from keyboard_listener import KeyboardListener

class KeyboardMonitor:
    def __init__(self):
        """Initialize a keyboard monitor that uses the KeyboardListener."""
        self.listener = KeyboardListener()
        self.is_running = False
        
    def start(self):
        """Start the keyboard monitoring."""
        # Subscribe to keyboard events
        self.subscription_id = self.listener.subscribe(self.on_keyboard_event)
        # Start listening for events
        self.listener.start_listening()
        self.is_running = True
        print("Keyboard monitoring started. Press Ctrl+C to exit.")
        
    def stop(self):
        """Stop the keyboard monitoring."""
        if self.is_running:
            # Stop listening and unsubscribe
            self.listener.stop_listening()
            self.listener.unsubscribe(self.subscription_id)
            self.is_running = False
            print("\nKeyboard monitoring stopped.")
    
    def on_keyboard_event(self, event_type, key):
        """
        Callback for keyboard events.
        
        Args:
            event_type (str): 'press' or 'release'
            key (str): Key name that triggered the event
        """
        print(f"Event: {event_type.ljust(7)} Key: {key}")
        
        # Optional: You can add special key handling here
        if event_type == 'press' and key == 'esc':
            print("Escape key pressed - exiting...")
            self.stop()
            return False  # Signal to exit the program


def main():
    monitor = KeyboardMonitor()
    try:
        monitor.start()
        # Keep the program running until Ctrl+C is pressed
        while monitor.is_running:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        monitor.stop()


if __name__ == "__main__":
    main()