import boto3


def listar_instancias():
    ec2 = boto3.client("ec2")
    regions = [region["RegionName"] for region in ec2.describe_regions()["Regions"]]

    for region in regions:
        regional_client = boto3.client("ec2", region_name=region)
        reservations = regional_client.describe_instances()["Reservations"]
        for reservation in reservations:
            for instance in reservation.get("Instances", []):
                instance_id = instance.get("InstanceId")
                instance_type = instance.get("InstanceType")
                state = instance.get("State", {}).get("Name")
                print(f"ID da Instância: {instance_id}\nTipo: {instance_type}\nEstado: {state}\nRegião: {region}\n")


if __name__ == "__main__":
    listar_instancias()
