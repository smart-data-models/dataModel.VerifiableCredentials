<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: LegalEntity  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Schema of an EBSI Verifiable ID for a legal entity**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `credentialSchema[object]`: Contains information about the credential schema (template) on which the Verifiable Authorisation is based  	- `id[uri]`: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
- `credentialStatus[object]`: Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)  	- `id[uri]`: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
	- `statusListCredential[uri]`: URL referencing the StatusList2021Credential    
	- `statusListIndex[string]`: Integer expressed as a string. The zero based index value identifies the bit position of the status    
	- `statusPurpose[string]`: Purpose of the status entry    
- `credentialSubject[object]`: Defines information about the subject that is described by the Verifiable ID  	- `EORI[string]`: Economic Operator Registration and Identification (EORI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1352/2013)    
	- `LEI[string]`: Official legal entity identifier (LEI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1247/2012)    
	- `SEED[string]`: System for Exchange of Excise Data (SEED) of Credential Subject (i.e. excise number provided in Article 2(12) of Council Regulation (EC) No 389/2012)    
	- `SIC[string]`: Standard Industrial Classification (SIC) of Credential Subject (Article 3(1) of Directive 2009/101/EC of the European Parliament and of the Council.)    
	- `VATRegistration[string]`: VAT number  of Credential Subject    
	- `domainName[string]`: Domain name  of Credential Subject    
	- `id[uri]`: Defines the DID of the subject that is described by the Verifiable Attestation    
	- `identifier[array]`: Description to be completed    
	- `legalAddress[string]`: Official legal address of Credential Subject    
	- `legalName[string]`: Official legal name of Credential Subject    
	- `legalPersonIdentifier[string]`: National/Legal Identifier of Credential Subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
- `evidence[array]`: Contains information about the process which resulted in the issuance of the Verifiable Attestation  - `expirationDate[date-time]`: Defines the date and time, when the Verifiable Attestation expires  - `id[uri]`: Defines unique identifier of the Verifiable Attestation  - `issuanceDate[date-time]`: Defines the date and time, when the Verifiable Attestation becomes valid  - `issued[date-time]`: Defines when the Verifiable Attestation was issued  - `issuer[uri]`: Defines the issuer of the Verifiable Attestation  - `proof[object]`: Contains information about the proof  	- `created[date-time]`: Defines the date and time, when the proof has been created    
	- `jws[string]`: Defines the proof value in JWS format    
	- `proofPurpose[string]`: Defines the purpose of the proof    
	- `type[string]`: Defines the proof type    
- `type[array]`: Defines the Verifiable Credential type  - `validFrom[date-time]`: Defines the date and time, when the Verifiable Attestation becomes valid  - `validUntil[date-time]`: Defines the date and time, when the Verifiable Attestation expires  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
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
LegalEntity:    
  description: Schema of an EBSI Verifiable ID for a legal entity    
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
      description: Defines information about the subject that is described by the Verifiable ID    
      properties:    
        EORI:    
          description: Economic Operator Registration and Identification (EORI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1352/2013)    
          type: string    
          x-ngsi:    
            type: Property    
        LEI:    
          description: Official legal entity identifier (LEI) of Credential Subject (referred to in Commission Implementing Regulation (EU) No 1247/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SEED:    
          description: System for Exchange of Excise Data (SEED) of Credential Subject (i.e. excise number provided in Article 2(12) of Council Regulation (EC) No 389/2012)    
          type: string    
          x-ngsi:    
            type: Property    
        SIC:    
          description: Standard Industrial Classification (SIC) of Credential Subject (Article 3(1) of Directive 2009/101/EC of the European Parliament and of the Council.)    
          type: string    
          x-ngsi:    
            type: Property    
        VATRegistration:    
          description: VAT number  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        domainName:    
          description: Domain name  of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        identifier:    
          description: Description to be completed    
          items:    
            properties:    
              id:    
                description: Description to be completed    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
              schemeID:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: Description to be completed    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
        legalAddress:    
          description: Official legal address of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalName:    
          description: Official legal name of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
        legalPersonIdentifier:    
          description: National/Legal Identifier of Credential Subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        taxReference:    
          description: Official tax reference number of Credential Subject    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - legalName    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          evidenceDocument:    
            items:    
              description: Description to be completed    
              type: string    
              x-ngsi:    
                type: Property    
            type: array    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found'    
            type: string    
            x-ngsi:    
              type: Property    
          subjectPresence:    
            description: Description to be completed    
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
    - credentialSubject    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/legal-entity/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/LegalEntity/LICENSE.md    
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
Not available the example of a LegalEntity in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
Not available the example of a LegalEntity in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
#### LegalEntity NGSI-LD key-values Example    
Here is an example of a LegalEntity in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://www.w3.org/2018/credentials/v1",  
    "https://europa.eu/schemas/v-id/2020/v1",  
    "https://europa.eu/schemas/eidas/2020/v1"  
  ],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation"],  
  "issuer": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3",  
  "issuanceDate": "2019-06-22T14:11:44Z",  
  "validFrom": "2019-06-22T14:11:44Z",  
  "issued": "2019-06-22T14:11:44Z",  
  "credentialSubject": {  
    "id": "did:ebsi:2659b154a445434a39d91149ead3bd993cb99fd5e78281b7",  
    "identifier": [  
      {  
        "schemeID": "SHACL",  
        "value": "SHACL ID 1",  
        "id": "http://student.id/41231232"  
      }  
    ],  
    "legalName": "Example Company"  
  },  
  "credentialStatus": {  
    "id": "https://europa.eu/status/identity#1dee355d-0432-4910-ac9c-70d89e8d674e",  
    "type": "CredentialStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://europa.eu/tsr-vid/verifiableid1.json",  
    "type": "FullJsonSchemaValidator2021"  
  },  
  "evidence": [  
    {  
      "id": "https://europa.eu/tsr-vid/evidence/f2aeec97-fc0d-42bf-8ca7-0548192d4231",  
      "type": ["DocumentVerification"],  
      "verifier": "did:ebsi:2e81454f76775c687694ee6772a17796436768a30e289555",  
      "evidenceDocument": ["Passport"],  
      "subjectPresence": "Physical",  
      "documentPresence": ["Physical"]  
    }  
  ],  
  "proof": {  
    "type": "EidasSeal2021",  
    "created": "2019-06-22T14:11:44Z",  
    "proofPurpose": "assertionMethod",  
    "verificationMethod": "did:ebsi:2757945549477fc571663bee12042873fe555b674bd294a3#2368332668",  
    "jws": "HG21J4fdlnBvBA+y6D...amP7O="  
  }  
}  
```  
</details>  
Not available the example of a LegalEntity in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
