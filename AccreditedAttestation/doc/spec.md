<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: AccreditedAttestation  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Schema of an EBSI Accredited Verifiable Attestation**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `credentialSchema[object]`: Contains information about the credential schema (template) on which the Verifiable Authorisation is based  - `credentialStatus[object]`: Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)  - `credentialSubject[object]`: Defines information about the subject that is described by the Verifiable Attestation  - `evidence[array]`: Contains information about the process which resulted in the issuance of the Verifiable Attestation  - `expirationDate[string]`: Defines the date and time, when the Verifiable Attestation expires  - `id[string]`: Defines unique identifier of the Verifiable Attestation  - `issuanceDate[string]`: Defines the date and time, when the Verifiable Attestation becomes valid  - `issued[string]`: Defines when the Verifiable Attestation was issued  - `issuer[string]`: Defines the issuer of the Verifiable Attestation  - `proof[object]`: Contains information about the proof  - `termsOfUse[array]`: Contains the terms under which the Accredited Verifiable Attestation was issued  - `type[array]`: Defines the Verifiable Credential type  - `validFrom[string]`: Defines the date and time, when the Verifiable Attestation becomes valid  - `validUntil[string]`: Defines the date and time, when the Verifiable Attestation expires  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Data models derived from EBSI json schemas https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. @context attribute has been removed from the definition because it is mandatory in NGSI-LD and does not need to be documented explicitly. Only available the example in key values linked data  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AccreditedAttestation:    
  description: Schema of an EBSI Accredited Verifiable Attestation    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: Property. References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
        type:    
          description: Property. Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
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
          description: Property. References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
        statusListCredential:    
          description: Property. URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
        statusListIndex:    
          description: Property. Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
        statusPurpose:    
          description: Property. Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
        type:    
          description: Property. Defines the Verifiable Credential status type    
          type: string    
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
          description: Property. Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Property. Description to be completed    
              type: string    
            type: array    
          evidenceDocument:    
            items:    
              description: Property. Description to be completed    
              type: string    
            type: array    
          id:    
            description: 'Property. If present, it MUST contain a URL that points to where more information about this instance of evidence can be found.'    
            type: string    
          subjectPresence:    
            description: Property. Description to be completed    
            type: string    
          type:    
            description: Property. Defines the evidence type    
            items:    
              type: string    
            type: array    
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
          description: 'Property. Defines the date and time, when the proof has been created'    
          format: date-time    
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
    termsOfUse:    
      description: Contains the terms under which the Accredited Verifiable Attestation was issued    
      items:    
        description: Property. Description to be completed    
        properties:    
          id:    
            description: Property. Contains a URL that points to where more information about this instance of terms of use can be found.    
            format: uri    
            type: string    
          type:    
            description: Property. Defines the type of terms of use.    
            type: string    
        required:    
          - id    
          - type    
        type: object    
      type: array    
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
  required: []    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-accredited-attestation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a AccreditedAttestation in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a AccreditedAttestation in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
#### AccreditedAttestation NGSI-LD key-values Example    
Here is an example of a AccreditedAttestation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:uuid:58afcb57-81f9-4e8c-817b-01f0597d6801",  
  "type": [  
    "VerifiableCredential",  
    "VerifiableAttestation",  
    "AccreditedVerifiableAttestation"  
  ],  
  "issuer": "did:ebsi:00001234",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "expirationDate": "2024-06-22T14:11:44Z",  
  "issued": "2020-06-22T14:11:44Z",  
  "termsOfUse": [  
    {  
      "id": "https://essif.europa.eu/accreditation/45",  
      "type": "VerifiableAccreditation"  
    }  
  ],  
  "credentialSubject": {  
    "id": "did:ebsi:00001235"  
  },  
  "credentialStatus": {  
    "id": "https://essif.europa.eu/status/45",  
    "type": "CredentialsStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0x4a131e78474b35ca4c93d4904cae9f2013cd53794ce521f6fcfac17ac460c6e5",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
Not available the example of a AccreditedAttestation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
