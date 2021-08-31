s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/


cd routes && tar zcf model.tar.gz model.py && aws s3 cp $PWD/model.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/model.tar.gz

cd routes && tar zcf model_1.tar.gz model_1.py && aws s3 cp $PWD/model_1.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/model_1.tar.gz

cd routes && tar zcf model_2.tar.gz model_2.py && aws s3 cp $PWD/model_2.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/model_2.tar.gz

cd routes && tar zcf model_3.tar.gz model_3.py && aws s3 cp $PWD/model_3.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/model_3.tar.gz

tar zcf model_4.tar.gz model_4.py && aws s3 cp $PWD/model_4.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/model_4.tar.gz

tar zcf covid.tar.gz covid.py && aws s3 cp $PWD/covid.tar.gz s3://tigermle-explorations/lenin/flask_on_sagemaker/multi_model/covid.tar.gz


---------------------------------

# The name of our algorithm
algorithm_name=demo-sagemaker-multimodel

cd container

account=$(aws sts get-caller-identity --query Account --output text)

# Get the region defined in the current configuration (default to us-west-2 if none defined)
region=$(aws configure get region)
region=${region:-us-west-2}

fullname="${account}.dkr.ecr.${region}.amazonaws.com/sagemaker:${algorithm_name}"


# If the repository doesn't exist in ECR, create it.
aws ecr describe-repositories --repository-names "${algorithm_name}" > /dev/null 2>&1


if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${algorithm_name}" > /dev/null
fi


# Get the login command from ECR and execute it directly
# $(aws ecr get-login --region ${region} --no-include-email)
aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com


# Build the docker image locally with the image name and then push it to ECR
# with the full name.


docker build -t ${algorithm_name} .
docker tag ${algorithm_name} ${fullname}

docker push ${fullname}


---------------------------