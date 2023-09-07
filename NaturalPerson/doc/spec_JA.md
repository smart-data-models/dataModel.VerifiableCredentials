<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ自然人  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/NaturalPerson/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**自然人の EBSI 検証可能 ID のスキーマ**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `credentialSchema[object]`: 検証可能な認証が基づくクレデンシャル・スキーマ（テンプレート）に関する情報が含まれる。  	- `id[uri]`: 検証可能な認可が基づく（関連する）信頼スキーマ・レジストリ（TSR）に格納されているクレ デンシャル・スキーマ（テンプレート）を参照する。    
- `credentialStatus[object]`: 検証可能な証明のステータスを確認する方法に関する情報を含む（失効および裏書レジストリ（RER）を通じて）。  	- `id[uri]`: 検証可能な認証の有効性を検証できるようにするため、失効および裏書レジストリ（RER）の 記録を参照する。    
	- `statusListCredential[uri]`: StatusList2021Credential を参照する URL。    
	- `statusListIndex[string]`: 文字列として表現される整数。ゼロベースのインデックス値は、ステータスのビット位置を示す。    
	- `statusPurpose[string]`: ステータスエントリーの目的    
- `credentialSubject[object]`: 検証可能IDによって記述される対象に関する追加情報を定義する。  	- `currentAddress[string]`: クレデンシャル・サブジェクトの現在のアドレスを定義する。    
	- `dateOfBirth[date]`: クレデンシャル対象者の生年月日を定義する。    
	- `familyName[string]`: クレデンシャル対象者の現在の姓を定義する。    
	- `firstName[string]`: クレデンシャル対象者の現在のファースト・ネームを定義する。    
	- `gender[string]`: クレデンシャル対象者の性別を定義する。    
	- `id[uri]`: 検証可能な証明によって記述される対象の DID を定義する。    
	- `nameAndFamilyNameAtBirth[string]`: クレデンシャル対象者の出生時の姓および名を定義する。    
	- `personalIdentifier[string]`: クレデンシャル対象者の一意の国内識別子（国境を越えた識別を目的とする技術仕様に 従って送信側加盟国が構築し、時間的に可能な限り永続的なもの）を定義する。    
- `evidence[array]`: 検証可能な証明書の発行に至ったプロセスに関する情報を含む。  - `expirationDate[date-time]`: 検証可能証明の有効期限が切れる日時を定義する。  - `id[uri]`: 検証可能証明の一意な識別子を定義する。  - `issuanceDate[date-time]`: 検証可能な認証が有効になる日時を定義する。  - `issued[date-time]`: 検証可能な証明書がいつ発行されたかを定義する。  - `issuer[uri]`: 検証可能な証明の発行者を定義する。  - `proof[object]`: 証明に関する情報を含む  	- `created[date-time]`: プルーフが作成された日時を定義します。    
	- `jws[string]`: JWSフォーマットで証明値を定義します。    
	- `proofPurpose[string]`: 証明の目的を明確にする    
	- `type[string]`: 証明タイプを定義する    
- `type[array]`: 検証可能クレデンシャルタイプを定義する。  - `validFrom[date-time]`: 検証可能な認証が有効になる日時を定義する。  - `validUntil[date-time]`: 検証可能証明の有効期限が切れる日時を定義する。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `credentialSubject`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
EBSI jsonスキーマから派生したデータモデル https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas.context属性はNGSI-LDでは必須であり、明示的に文書化する必要がないため、定義から削除された。キー値リンクデータの例のみ利用可能  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
キー値として JSON-LD 形式の NaturalPerson の例は利用できません。これは、`options=keyValues` を使用している場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
正規化された JSON-LD 形式の NaturalPerson の例はありません。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。  
#### NaturalPerson NGSI-LD キー値の例  
以下は、キー値として JSON-LD フォーマットの NaturalPerson の例です。これは、`options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
正規化された JSON-LD 形式の NaturalPerson の例はありません。これは、オプションを使用しない場合は NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
