<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Atestado  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/Attestation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esquema de un certificado verificable EBSI**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `credentialSchema[object]`: Contiene información sobre el esquema de credenciales (plantilla) en el que se basa la autorización verificable  	- `id[uri]`: Hace referencia al esquema de credenciales (plantilla) almacenado en el Registro de Esquemas de Confianza (TSR) (pertinente) en el que se basa la Autorización Verificable.    
- `credentialStatus[object]`: Contiene información sobre cómo verificar el estado de la atestación verificable (a través del Registro de Revocación y Refrendo, RER)  	- `id[uri]`: Registro de referencias en el Registro de revocaciones y refrendos (RER) para permitir la verificación de la validez de un certificado verificable.    
	- `statusListCredential[uri]`: URL que hace referencia a StatusList2021Credential    
	- `statusListIndex[string]`: Número entero expresado como cadena. El valor del índice basado en cero identifica la posición del bit del estado    
	- `statusPurpose[string]`: Finalidad de la entrada de estado    
- `credentialSubject[object]`: Define la información sobre el sujeto que se describe en el certificado verificable.  	  
- `evidence[array]`: Contiene información sobre el proceso que dio lugar a la emisión del certificado verificable  - `expirationDate[date-time]`: Define la fecha y hora en que expira el certificado verificable.  - `id[uri]`: Define el identificador único del certificado verificable  - `issuanceDate[date-time]`: Define la fecha y hora en que el certificado verificable pasa a ser válido.  - `issued[date-time]`: Define cuándo se emitió el certificado verificable  - `issuer[uri]`: Define el emisor del certificado verificable  - `proof[object]`: Contiene información sobre la prueba  	- `created[date-time]`: Define la fecha y la hora de creación de la prueba.    
	- `jws[string]`: Define el valor de la prueba en formato JWS    
	- `proofPurpose[string]`: Define el objetivo de la prueba    
	- `type[string]`: Define el tipo de prueba    
- `type[array]`: Define el tipo de credencial verificable  - `validFrom[date-time]`: Define la fecha y hora en que el certificado verificable pasa a ser válido.  - `validUntil[date-time]`: Define la fecha y hora en que expira el certificado verificable.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `credentialSchema`  - `credentialSubject`  - `id`  - `issuanceDate`  - `issued`  - `issuer`  - `type`  - `validFrom`  <!-- /35-RequiredProperties -->  
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
Attestation:    
  description: Schema of an EBSI Verifiable Attestation    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListCredential:    
          description: URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListIndex:    
          description: Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
          x-ngsi:    
            type: Property    
        statusPurpose:    
          description: Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the Verifiable Credential status type    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines information about the subject that is described by the Verifiable Attestation    
      properties:    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found.'    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the evidence type    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        jws:    
          description: Defines the proof value in JWS format    
          type: string    
          x-ngsi:    
            type: Property    
        proofPurpose:    
          description: Defines the purpose of the proof    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the proof type    
          type: string    
          x-ngsi:    
            type: Property    
        verificationMethod:    
          description: Contains information about the verification method / proof mechanisms    
          type: string    
          x-ngsi:    
            type: Property    
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
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - issuer    
    - issuanceDate    
    - issued    
    - validFrom    
    - credentialSubject    
    - credentialSchema    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-attestation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/Attestation/LICENSE.md    
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
No disponible el ejemplo de un Attestation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
No disponible el ejemplo de un Atestado en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
#### Attestation NGSI-LD key-values Ejemplo  
A continuación se muestra un ejemplo de un Attestation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:uuid:003a1dd8-a5d2-42ef-8182-e921c0a9f2cd",  
  "type": ["VerifiableCredential", "VerifiableAttestation"],  
  "issuer": "did:ebsi:00001234",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "expirationDate": "2024-06-22T14:11:44Z",  
  "issued": "2020-06-22T14:11:44Z",  
  "credentialSubject": {  
    "id": "did:ebsi:00001235"  
  },  
  "credentialStatus": {  
    "id": "https://api-test.ebsi.eu/trusted-issuers-registry/v3/issuers/did:ebsi:zyrMG8T9xYbNoSwyQa4SGMJ/proxy/6cc5fcc621d8098977d378ec7bf63f9ad0b204d56bb604f75bc9290e7033ac84/credentials/status/5#129430",  
    "type": "StatusList2021Entry",  
    "statusPurpose": "revocation",  
    "statusListIndex": "129430",  
    "statusListCredential": "https://api-test.ebsi.eu/trusted-issuers-registry/v3/issuers/did:ebsi:zyrMG8T9xYbNoSwyQa4SGMJ/proxy/6cc5fcc621d8098977d378ec7bf63f9ad0b204d56bb604f75bc9290e7033ac84/credentials/status/5"  
  },  
  "credentialSchema": {  
    "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0xf30fd418c8b2c1534b0685e12b044d3d29284fe37762a45d0c1e5601eed3d1d9",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
No está disponible el ejemplo de un Atestado en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
