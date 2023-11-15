import launch

if not launch.is_installed("BytesIO"):
    launch.run_pip("install BytesIO", "requirements for image conversion to send to rubbrband")