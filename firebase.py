import firebase_admin
from firebase_admin import credentials, storage
import datetime
import requests


class StorageImgFirebase:
    def __init__(self) -> None:
        pass

    def uploadImg(
        self,
        patchnamelocal="document.pdf",
        patchnameFirebase="/img/document.pdf",
        nameOfBucket="cancerdetectionimg.appspot.com",
    ):
        # Initialisez Firebase avec vos identifiants
        cred = credentials.Certificate(
            "cancerdetectionimg-firebase-adminsdk-qhz6b-ee93691b55.json"
        )
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "cancerdetectionimg-firebase-adminsdk-qhz6b-ee93691b55.json"
            )
            firebase_admin.initialize_app(
                cred,
                {
                    "storageBucket": "cancerdetectionimg.appspot.com"  # Remplacez par l'URL de votre bucket de stockage Firebase
                },
            )

        # Initialisez le client de stockage
        bucket = storage.bucket()

        # Chemin local du fichier PDF que vous souhaitez uploader
        local_file_path = patchnamelocal

        # Nom du fichier sur Firebase Storage (peut être le même que le nom local)
        firebase_storage_path = patchnameFirebase

        # Upload du fichier PDF
        blob = bucket.blob(firebase_storage_path)

        blob.upload_from_filename(local_file_path)

        print("Fichier PDF uploadé avec succès sur Firebase Storage.")

    def DownloadUrl(self, pathFromFirebase):
        # Initialisez Firebase avec vos identifiants (vérifiez si l'application n'est pas déjà initialisée)
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "cancerdetectionimg-firebase-adminsdk-qhz6b-ee93691b55.json"
            )
            firebase_admin.initialize_app(
                cred,
                {
                    "storageBucket": "cancerdetectionimg.appspot.com"  # Remplacez par l'URL de votre bucket de stockage Firebase
                },
            )

        # Initialisez le client de stockage
        bucket = storage.bucket()

        # Chemin sur Firebase Storage du fichier que vous souhaitez télécharger
        firebase_storage_path = pathFromFirebase

        # Créer une URL signée pour le téléchargement du fichier
        blob = bucket.blob(firebase_storage_path)

        expiration = datetime.timedelta(
            days=1
        )  # Définir une durée de validité d'un jour pour l'URL (modifiable selon vos besoins)

        url = blob.generate_signed_url(expiration=expiration)

        return url

    def dowloadimage(self, image_url):
        # Faire une requête GET pour récupérer l'image à partir de l'URL
        response = requests.get(image_url)

        if response.status_code == 200:
            # L'image a été récupérée avec succès
            image_data = response.content
            return image_data
        else:
            # Gérer les erreurs de récupération de l'image
            return "Erreur lors de la récupération de l'image"
