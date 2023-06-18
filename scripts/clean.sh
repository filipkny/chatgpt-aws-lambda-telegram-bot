if [ -d ".aws-sam" ]; then rm -rf .aws-sam; fi
if [ -f "requirements.txt" ]; then rm requirements.txt; fi
if [ -d "package" ]; then rm -rf package; fi
if [ -f "packaged.yaml" ]; then rm packaged.yaml; fi
