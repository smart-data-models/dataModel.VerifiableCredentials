<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 자연인  
========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **자연인에 대한 EBSI 검증 가능한 ID 스키마**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `credentialSchema[object]`: 확인 가능한 인증의 기반이 되는 자격 증명 스키마(템플릿)에 대한 정보를 포함합니다.  	- `id[uri]`: 확인 가능한 인증의 기반이 되는 (관련) TSR(신뢰할 수 있는 스키마 레지스트리)에 저장된 자격 증명 스키마(템플릿)를 참조합니다.    
	- `type[string]`: 자격 증명 스키마 유형 정의    
- `credentialStatus[object]`: (취소 및 승인 레지스트리, RER을 통해) 확인 가능한 증명의 상태를 확인하는 방법에 대한 정보가 포함되어 있습니다.  	- `id[uri]`: 검증 가능한 증명의 유효성을 확인할 수 있도록 취소 및 승인 레지스트리(RER)에 레퍼런스를 기록합니다.    
	- `statusListCredential[uri]`: StatusList2021Credential을 참조하는 URL    
	- `statusListIndex[string]`: 문자열로 표현된 정수입니다. 0을 기준으로 하는 인덱스 값은 상태의 비트 위치를 식별합니다.    
	- `statusPurpose[string]`: 상태 항목의 목적    
	- `type[string]`: 확인 가능한 자격증명 상태 유형을 정의합니다.    
- `credentialSubject[object]`: 확인 가능한 ID로 설명되는 대상에 대한 추가 정보를 정의합니다.  	- `currentAddress[string]`: 자격 증명 주체의 현재 주소를 정의합니다.    
	- `dateOfBirth[date]`: 자격 증명 주체의 생년월일을 정의합니다.    
	- `familyName[string]`: 자격 증명 주체의 현재 성을 정의합니다.    
	- `firstName[string]`: 자격 증명 주체의 현재 이름을 정의합니다.    
	- `gender[string]`: 자격 증명 주체의 성별을 정의합니다.    
	- `id[uri]`: 검증 가능한 증명이 설명하는 주체의 DID를 정의합니다.    
	- `nameAndFamilyNameAtBirth[string]`: 자격 증명 주체의 출생 시 이름과 가족 이름을 정의합니다.    
	- `personalIdentifier[string]`: 자격 증명 주체의 고유한 국가 식별자(송신 회원국이 국경 간 식별을 목적으로 기술 사양에 따라 구성하고 가능한 한 영구적으로 유지되는)를 정의합니다.    
	- `placeOfBirth[string]`: 자격 증명 주체가 태어난 곳을 정의합니다.    
- `evidence[array]`: 검증 가능한 증명이 발급된 프로세스에 대한 정보를 포함합니다.  - `expirationDate[date-time]`: 검증 가능한 증명이 만료되는 날짜와 시간을 정의합니다.  - `id[uri]`: 검증 가능한 증명의 고유 식별자를 정의합니다.  - `issuanceDate[date-time]`: 검증 가능한 증명이 유효해지는 날짜와 시간을 정의합니다.  - `issued[date-time]`: 확인 가능한 증명이 발행된 시점을 정의합니다.  - `issuer[uri]`: 검증 가능한 증명의 발급자를 정의합니다.  - `proof[object]`: 증명에 대한 정보를 포함합니다.  	- `created[date-time]`: 증명이 생성된 날짜와 시간을 정의합니다.    
	- `jws[string]`: JWS 형식으로 증명 값을 정의합니다.    
	- `proofPurpose[string]`: 증명의 목적을 정의합니다.    
	- `type[string]`: 증명 유형을 정의합니다.    
	- `verificationMethod[string]`: 인증 방법/증명 메커니즘에 대한 정보를 포함합니다.    
- `type[array]`: 확인 가능한 자격증명 유형을 정의합니다.  - `validFrom[date-time]`: 검증 가능한 증명이 유효해지는 날짜와 시간을 정의합니다.  - `validUntil[date-time]`: 검증 가능한 증명이 만료되는 날짜와 시간을 정의합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
EBSI json 스키마에서 파생된 데이터 모델 https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas. 컨텍스트 속성은 NGSI-LD에서 필수이며 명시적으로 문서화할 필요가 없으므로 정의에서 제거되었습니다. 키 값 연결 데이터에서만 예제 사용 가능  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NaturalPerson:    
  description: Schema of an EBSI Verifiable ID for a natural person    
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
      description: Defines additional information about the subject that is described by the Verifiable ID    
      properties:    
        currentAddress:    
          description: Defines the current address of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        dateOfBirth:    
          description: Defines date of birth of the credential subject    
          format: date    
          type: string    
          x-ngsi:    
            type: Property    
        familyName:    
          description: Defines current family name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        firstName:    
          description: Defines current first name(s) of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        gender:    
          description: Defines the gender of the credential subject    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        nameAndFamilyNameAtBirth:    
          description: Defines the first and the family name(s) of the credential subject at the time of their birth    
          type: string    
          x-ngsi:    
            type: Property    
        personalIdentifier:    
          description: Defines the unique national identifier of the credential subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)    
          type: string    
          x-ngsi:    
            type: Property    
        placeOfBirth:    
          description: Defines the place where the credential subjectis born    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - familyName    
        - firstName    
        - dateOfBirth    
        - personalIdentifier    
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
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-vid/natural-person/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
JSON-LD 형식의 NaturalPerson 예제를 키 값으로 사용할 수 없습니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
정규화된 JSON-LD 형식의 NaturalPerson 예제를 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
#### NaturalPerson NGSI-LD 키-값 예시  
다음은 JSON-LD 형식의 NaturalPerson을 키값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:did:123456",  
  "type": ["VerifiableCredential", "VerifiableAttestation", "VerifiableId"],  
  "issuer": "urn:did:9999999",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "issued": "2021-11-01T00:00:00Z",  
  "credentialSubject": {  
    "id": "urn:uri:123",  
    "personalIdentifier": "IT/DE/1234",  
    "familyName": "Castafiori",  
    "firstName": "Bianca",  
    "dateOfBirth": "1930-10-01"  
  },  
  "credentialSchema": {  
    "id": "https://permanent.url.of/vid/naturalperson",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
정규화된 JSON-LD 형식의 NaturalPerson 예제를 사용할 수 없습니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
