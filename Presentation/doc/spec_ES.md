<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Presentación  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/Presentation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esquema de una presentación verificable EBSI**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `holder[string]`: Define el identificador único de la parte que comparte la Presentación Verificable  - `proof[object]`: Contiene información sobre la prueba  - `type[array]`: Define el tipo de presentación verificable  - `verifiableCredential[array]`: Contiene la información personal que se pretende compartir  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `holder`  - `type`  - `verifiableCredential`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Modelos de datos derivados de esquemas json EBSI https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. El atributo @context se ha eliminado de la definición porque es obligatorio en NGSI-LD y no es necesario documentarlo explícitamente. Sólo está disponible el ejemplo en datos enlazados con valores clave  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Presentation:    
  description: Schema of an EBSI Verifiable Presentation    
  properties:    
    holder:    
      description: Defines unique identifier of the party who shares the Verifiable Presentation    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        challenge:    
          description: Property. Defines a random or pseudo-random value used by some authentication protocols to mitigate replay attacks    
          type: string    
        created:    
          description: 'Property. Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
        domain:    
          description: Property. Defines a string value that specifies the operational domain of a digital proof    
          format: hostname    
          type: string    
        jws:    
          description: Property. Defines the proof value in JWS format    
          type: string    
        proofPurpose:    
          description: Property. Defines the purpose of the proof    
          type: string    
        type:    
          description: Property. Defines the proof type    
          type: string    
        verificationMethod:    
          description: Property. Contains information about the verification method / proof mechanisms    
          type: string    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Presentation type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    verifiableCredential:    
      description: Contains the personal information intended to be shared    
      items:    
        oneOf:    
          - credentialSchema:    
              description: Property. Description to be completed    
              properties:    
                id:    
                  description: Property. Description to be completed    
                  type: string    
                type:    
                  description: Property. Description to be completed    
                  type: string    
              type: object    
            properties:    
              credentialSubject:    
                dateOfBirth:    
                  description: Property. Description to be completed    
                  format: Date    
                  type: string    
                familyName:    
                  description: Property. Description to be completed    
                  type: string    
                firstName:    
                  description: Property. Description to be completed    
                  type: string    
                id:    
                  description: Property. Description to be completed    
                  format: uri    
                  type: string    
                personalIdentifier:    
                  description: Property. Description to be completed    
                  type: string    
              id:    
                description: Property. Description to be completed    
                format: uri    
                type: string    
              issuanceDate:    
                description: Property. Description to be completed    
                format: date-time    
                type: string    
              issuer:    
                description: Property. Description to be completed    
                type: string    
              type:    
                description: Property. Description to be completed    
                items:    
                  type: string    
                type: array    
              validFrom:    
                description: Property. Description to be completed    
                format: date-time    
                type: string    
            type: object    
          - type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - holder    
    - verifiableCredential    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-presentation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/Presentation/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
No disponible el ejemplo de una Presentación en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una Presentación en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
#### Presentación NGSI-LD key-values Ejemplo  
He aquí un ejemplo de Presentación en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
No está disponible el ejemplo de una Presentación en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
