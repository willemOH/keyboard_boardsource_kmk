import storage
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "4X12"
storage.remount("/", readonly=True)
storage.enable_usb_drive()
