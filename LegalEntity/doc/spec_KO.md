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
- `credentialSubject[object]`: 확인 가능한 ID로 설명되는 대상에 대한 정보를 정의합니다.  
	- `LEI[string]`: 자격 증명 주체의 공식 법인식별기호(LEI)(유럽 연합 집행위원회 시행 규정 (EU) 제1247/2012호 참조)    
	- `SEED[string]`: 자격 증명 주체의 소비세 데이터 교환 시스템(SEED)(즉, 이사회 규정(EC) 제389/2012호 제2조(12)에 규정된 소비세 번호)    
	- `SIC[string]`: 자격 증명 주체의 표준 산업 분류(SIC)(유럽 의회 및 이사회 지침 2009/101/EC 제3조 1항).    
	- `VATRegistration[string]`: 자격 증명 주체의 부가가치세 번호    
	- `domainName[string]`: 자격 증명 주체의 도메인 이름    
	- `id[uri]`: 검증 가능한 증명이 설명하는 주체의 DID를 정의합니다.    
	- `identifier[array]`: 입력할 설명    
	- `legalAddress[string]`: 자격 증명 주체의 공식 법적 주소    
	- `legalName[string]`: 자격 증명 주체의 공식 법적 이름    
	- `legalPersonIdentifier[string]`: 자격 증명 주체의 국가/법적 식별자(송신 회원국이 국경 간 식별을 목적으로 기술 사양에 따라 구성하고 가능한 한 시간 내에 지속되는 식별자)    
	- `taxReference[string]`: 자격 증명 주체의 공식 세금 참조 번호    
- `evidence[array]`: 검증 가능한 증명이 발급된 프로세스에 대한 정보를 포함합니다.  
	- `jws[string]`: JWS 형식으로 증명 값을 정의합니다.    
	- `proofPurpose[string]`: 증명의 목적을 정의합니다.    
	- `type[string]`: 증명 유형을 정의합니다.    
	- `verificationMethod[string]`: 인증 방법/증명 메커니즘에 대한 정보를 포함합니다.    
- `type[array]`: 확인 가능한 자격증명 유형을 정의합니다.  
<!-- 35-RequiredProperties -->

- `credentialSubject`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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





<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
