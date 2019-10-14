## Installation Instructions

1. Mkdir Dev in a Desktop folder. 
2. Open Powershell and navigate to that folder. 
3. run virtualenv RecycleTech_env (This will create a virtual env in this dir)
4. cd into this new folder: cd RecycleTech_env
5. mkdir RecycleTech_SRC
6. cd RecycleTech_SRC
7. Open Sourcetree (download it here: https://product-downloads.atlassian.com/software/sourcetree/ga/Sourcetree_3.2_224.zip)
8. Click the plus add: and clone. Enter https://github.com/Rangrom182/RecycleTech_Inv.git
9. Choose that RecycleTech_SRC folder to clone it to that location.
10. In powershell go back to the Virtual folder RecycleTech_env
11. run .\scripts\activate
12. Move the requirements.txt into the environment folder. 
13. In powershell to install Packages for VirtualEnv run: pip install -r requirements.txt (Given you are in the path cd)
