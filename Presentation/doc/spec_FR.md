<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Présentation  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/Presentation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- Aucune propriété requise  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Modèle de données dérivé des schémas EBSI json https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. Seul l'exemple des données liées aux valeurs clés est disponible  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
Non disponible l'exemple d'une présentation au format JSON-LD comme valeurs-clés. Ceci est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
Non disponible l'exemple d'une présentation au format JSON-LD tel que normalisé. Cette présentation est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
#### Présentation des valeurs clés NGSI-LD Exemple  
Voici un exemple de présentation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://www.w3.org/2018/credentials/v1"  
  ],  
  "type": [  
    "VerifiablePresentation"  
  ],  
  "holder": "did:ebsi:00012345",  
  "verifiableCredential": [  
    {  
      "@context": [  
        "https://www.w3.org/2018/credentials/v1"  
      ],  
      "id": "urn:uuid:b5bf4778-b8f5-4d76-aa0d-aab46ae9a8fe",  
      "type": [  
        "VerifiableCredential",  
        "VerifiableAttestation",  
        "VerifiableId"  
      ],  
      "issuer": "did:ebsi:0001234",  
      "issuanceDate": "2021-11-41T00:00:00Z",  
      "validFrom": "2021-11-01T00:00:00Z",  
      "credentialSubject": {  
        "id": "did:ebsi:00012345",  
        "personalIdentifier": "IT/DE/1234",  
        "familyName": "Castafiori",  
        "firstName": "Bianca",  
        "dateOfBirth": "1930-10-01"  
      },  
      "credentialSchema": {  
        "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0xad457662a535791e888994e97d7b5e0cdd09fbae2c8900039d2ee2d9a64969b1",  
        "type": "FullJsonSchemaValidator2021"  
      }  
    },  
    {  
      "@context": [  
        "https://www.w3.org/2018/credentials/v1"  
      ],  
      "id": "urn:uuid:8ebaad40-6b85-41d6-b7e8-86f2b5fc2b31",  
      "type": [  
        "VerifiableCredential",  
        "VerifiableAttestation"  
      ],  
      "issuer": "did:ebsi:0001234",  
      "issuanceDate": "2021-10-31T00:00:00Z",  
      "validFrom": "2021-11-01T00:00:00Z",  
      "credentialSubject": {  
        "id": "did:ebsi:00012345"  
      },  
      "credentialSchema": {  
        "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0x28d76954924d1c4747a4f1f9e3e9edc9ca965efbf8ff20e4339c2bf2323a5773",  
        "type": "FullJsonSchemaValidator2021"  
      }  
    }  
  ],  
  "proof": {  
    "type": "",  
    "proofPurpose": "",  
    "created": "2021-10-31T00:00:00Z",  
    "verificationMethod": "",  
    "jws": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImRpZDplYnNpOnp2SFdYMzU5QTNDdmZKbkNZYUFpQWRlI0YwcjVPeXRfbGFodnZ6Nk1XbFlzM21jWU5LWmlpUWRVZnF2OHRzaEhOOXcifQ.eyJpc3MiOiJkaWQ6ZWJzaTp6dkhXWDM1OUEzQ3ZmSm5DWWFBaUFkZSIsInN1YiI6ImRpZDplYnNpOnpkUGoxR1BYamZFUlh4WFBFMVlUWWRKIiwiaWF0IjoiMjAyMC0wNi0yMlQxNDoxMTo0NFoiLCJuYmYiOiIyMDIxLTExLTAxVDAwOjAwOjAwWiIsImp0aSI6InVybjp1dWlkOjA4ZTI2ZDIyLThkY2EtNDU1OC05YzE0LTZlN2FhNzI3NWI5YiIsInZjIjp7IkBjb250ZXh0IjpbImh0dHBzOi8vd3d3LnczLm9yZy8yMDE4L2NyZWRlbnRpYWxzL3YxIl0sImlkIjoidXJuOnV1aWQ6MDhlMjZkMjItOGRjYS00NTU4LTljMTQtNmU3YWE3Mjc1YjliIiwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIlZlcmlmaWFibGVBdHRlc3RhdGlvbiIsIlZlcmlmaWFibGVBdXRob3Jpc2F0aW9uIl0sImlzc3VlciI6ImRpZDplYnNpOnp2SFdYMzU5QTNDdmZKbkNZYUFpQWRlIiwiaXNzdWFuY2VEYXRlIjoiMjAyMS0xMS0wMVQwMDowMDowMFoiLCJ2YWxpZEZyb20iOiIyMDIxLTExLTAxVDAwOjAwOjAwWiIsImV4cGlyYXRpb25EYXRlIjoiMjAyNC0wNi0yMlQxNDoxMTo0NFoiLCJpc3N1ZWQiOiIyMDIwLTA2LTIyVDE0OjExOjQ0WiIsImNyZWRlbnRpYWxTdWJqZWN0Ijp7ImlkIjoiZGlkOmVic2k6emRQajFHUFhqZkVSWHhYUEUxWVRZZEoiLCJhY2Nlc3MiOlsib25ib2FyZCJdfSwiY3JlZGVudGlhbFN0YXR1cyI6eyJpZCI6Imh0dHBzOi8vYXBpLnByZXByb2QuZWJzaS5ldS90cnVzdGVkLWlzc3VlcnMtcmVnaXN0cnkvdjMvaXNzdWVycy9kaWQ6ZWJzaTp6eXJNRzhUOXhZYk5vU3d5UWE0U0dNSi9wcm94eS82Y2M1ZmNjNjIxZDgwOTg5NzdkMzc4ZWM3YmY2M2Y5YWQwYjIwNGQ1NmJiNjA0Zjc1YmM5MjkwZTcwMzNhYzg0L2NyZWRlbnRpYWxzL3N0YXR1cy81IzEyOTQzMCIsInR5cGUiOiJTdGF0dXNMaXN0MjAyMUVudHJ5Iiwic3RhdHVzUHVycG9zZSI6InJldm9jYXRpb24iLCJzdGF0dXNMaXN0SW5kZXgiOiIxMjkyMzAiLCJzdGF0dXNMaXN0Q3JlZGVudGlhbCI6Imh0dHBzOi8vYXBpLnByZXByb2QuZWJzaS5ldS90cnVzdGVkLWlzc3VlcnMtcmVnaXN0cnkvdjMvaXNzdWVycy9kaWQ6ZWJzaTp6eXJNRzhUOXhZYk5vU3d5UWE0U0dNSi9wcm94eS82Y2M1ZmNjNjIxZDgwOTg5NzdkMzc4ZWM3YmY2M2Y5YWQwYjIwNGQ1NmJiNjA0Zjc1YmM5MjkwZTcwMzNhYzg0L2NyZWRlbnRpYWxzL3N0YXR1cy81In0sImNyZWRlbnRpYWxTY2hlbWEiOnsiaWQiOiJodHRwczovL2FwaS5wcmVwcm9kLmVic2kuZXUvdHJ1c3RlZC1zY2hlbWFzLXJlZ2lzdHJ5L3YxL3NjaGVtYXMvMHg5MGJiYjVlMGViZWU2NTM4Y2RhZTQ0ZGI5YTZmOGMzOGQ4NWM1YTRkNjllOTJlMGM2MzNlYTE5ZTVhZWIxOTdmIiwidHlwZSI6IkZ1bGxKc29uU2NoZW1hVmFsaWRhdG9yMjAyMSJ9fX0.H6BFgrl8bAvGsLCk4gD12DIfUKH2W8gI2cFuRbF6eGV7fciGsr1XLxWp6jM4l9fuDXBQ6BLSVhZQR2B4uqIIrA"  
  }  
}  
```  
</details>  
Non disponible l'exemple d'une présentation au format JSON-LD comme normalisé. Cette présentation est compatible avec NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
