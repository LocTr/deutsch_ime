import keyboard

class KeyboardListener:
    def __init__(self):
        """Initialize a keyboard listener."""
        self.is_listening = False
        self.hooks = []
        self.event_subscribers = []

    def start_listening(self):
        """Start listening for keyboard events."""
        if not self.is_listening:
            # Hook for key press events
            self.hooks.append(keyboard.on_press(self._on_press_event))
            # Hook for key release events
            self.hooks.append(keyboard.on_release(self._on_release_event))
            self.is_listening = True

    def stop_listening(self):
        """Stop listening for keyboard events."""
        if self.is_listening:
            for hook in self.hooks:
                keyboard.unhook(hook)
            self.hooks = []
            self.is_listening = False

    def subscribe(self, callback):
        """
        Subscribe to keyboard events.
        
        Args:
            callback (callable): Function called with (event_type, key) arguments
                where event_type is 'press' or 'release' and key is the key name.
                
        Returns:
            int: Subscription ID for unsubscribing.
        """
        self.event_subscribers.append(callback)
        return len(self.event_subscribers) - 1

    def unsubscribe(self, subscription_id):
        """
        Unsubscribe from keyboard events.
        
        Args:
            subscription_id (int): ID returned by subscribe().
        """
        if 0 <= subscription_id < len(self.event_subscribers):
            self.event_subscribers[subscription_id] = None

    def _on_press_event(self, event):
        """Handle key press events."""
        for subscriber in self.event_subscribers:
            if subscriber:
                subscriber('press', event.name)

    def _on_release_event(self, event):
        """Handle key release events."""
        for subscriber in self.event_subscribers:
            if subscriber:
                subscriber('release', event.name)