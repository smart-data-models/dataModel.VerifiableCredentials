<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `credentialSchema[object]`: 확인 가능한 인증의 기반이 되는 자격 증명 스키마(템플릿)에 대한 정보를 포함합니다.  
	- `type[string]`: 자격 증명 스키마 유형 정의    
- `credentialStatus[object]`: (취소 및 승인 레지스트리, RER을 통해) 확인 가능한 증명의 상태를 확인하는 방법에 대한 정보가 포함되어 있습니다.  
	- `statusListCredential[uri]`: StatusList2021Credential을 참조하는 URL    
	- `statusListIndex[string]`: 문자열로 표현된 정수입니다. 0을 기준으로 하는 인덱스 값은 상태의 비트 위치를 식별합니다.    
	- `statusPurpose[string]`: 상태 항목의 목적    
	- `type[string]`: 확인 가능한 자격증명 상태 유형을 정의합니다.    
- `credentialSubject[object]`: 검증 가능한 증명이 설명하는 대상에 대한 정보를 정의합니다.  
- `evidence[array]`: 검증 가능한 증명이 발급된 프로세스에 대한 정보를 포함합니다.  
	- `jws[string]`: JWS 형식으로 증명 값을 정의합니다.    
	- `proofPurpose[string]`: 증명의 목적을 정의합니다.    
	- `type[string]`: 증명 유형을 정의합니다.    
	- `verificationMethod[string]`: 인증 방법/증명 메커니즘에 대한 정보를 포함합니다.    
- `type[array]`: 확인 가능한 자격증명 유형을 정의합니다.  
<!-- 35-RequiredProperties -->

- `credentialSchema`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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





<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
