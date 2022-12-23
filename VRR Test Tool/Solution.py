import tkinter as tk
import win32api


class RefreshRateMonitor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Refresh rate:")
        self.label.pack()
        self.refresh_rate_timer = self.after(1000, self.update_refresh_rate)

    def update_refresh_rate(self):
        refresh_rate = get_refresh_rate(None)
        self.label.config(text=f"Refresh rate: {refresh_rate} Hz")
        self.refresh_rate_timer = self.after(1000, self.update_refresh_rate)


def get_refresh_rate(device_name):
    display_settings = win32api.EnumDisplaySettings(device_name, -1)
    refresh_rate = display_settings.DisplayFrequency
    return refresh_rate


app = RefreshRateMonitor()
app.mainloop()
