import boto3

def ejecutar_reporte():
    # Conectarse a S3
    s3 = boto3.client('s3')
    
    # 1. Listar buckets
    print("=== LISTA DE BUCKETS S3 ===")
    response = s3.list_buckets()
    buckets = [b['Name'] for b in response['Buckets']]
    
    for nombre in buckets:
        print(f"Bucket: {nombre}")
        
        # 2. Listar objetos dentro de cada bucket
        print(f"  Contenido de {nombre}:")
        objetos = s3.list_objects_v2(Bucket=nombre)
        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"    - {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("    [Bucket vacío]")
    print("===========================")

if __name__ == "__main__":
    ejecutar_reporte()
