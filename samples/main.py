
""" To document """

from screenflow import ScreenFlow


class Application(ScreenFlow):
    """ Simple wifi connect application """
    def __init__(self):
        # Configure second screen.
        self.wifi_select.provider = get_wifi_networks
        self.wifi_select.renderer = None # TODO Set custom renderer.
        self.wifi_select.listener = None # TODO : Switch to view.
        self.wifi_select.on_select(self.navigate_to(self.wifi_passphrase))

screenflow = Screenflow()
screenflow.primary_font = None
screenflow.secondary_font = None
screenflow.load_from_file('test.xml')

@screenflow.wifi_prompt.on_select
def on_wifi_prompt(option):
    """On user action """
    if option == 'yes':
        screenflow.navigate_to(screenflow.wifi_select)
    elif option == 'no':
        screenflow.quit()

@screenflow.wifi_select.provider
def get_wifi_networks():
    """Returns wifi network. """
    return None

@screenflow.wifi_select.on_click
def set_wifi():
    """Set wifi and quit. """
    pass

if __name__ == '__main__':
    screenflow.run()