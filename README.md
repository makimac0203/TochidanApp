# TochidanApp
ダンスイベントのアーティストエントリー用のアプリケーションです。使用BGM、アーティスト写真、チーム構成などの主要な項目をアップロードして、管理者が容易に確認できるようにすることが目的です。


<br>
<br>


## 拘ったところ
<ul>
  <li>ユーザーが音源をアップロードすると再生をして内容をすぐ確認できる、これにより間違った曲のアップロードのミスが防げる</li>
  <li>管理者ログインは一般ユーザーと同じログインフォームで管理者権限により遷移先を切り替えている、別に管理者用のログインフォーム用意する手間が省ける</li>
  <li>管理者はログインするとエントリーユーザー一覧を確認することができ、全てのユーザーの詳細ページに入って音源の確認、ダウンロードができる</li>
  <li>ユーザーは新規アカウント登録をしたあと、詳細ページを埋めて登録しないと、先に進めないようになっている、再度ログインすると詳細登録ページに遷移するようになっているので、最終エントリーまでの動線ができている。</li>
</ul>
<br>
<br>

## 本番環境での使用技術
<ul>  
  <li>AWS(ES2, RDS(PostgreSQL), S3)</li>
  <li>Nginx</li>
  <li>Ubuntu</li>
  <li>SendGrid</li>
</ul>
<br>
<br>


## トップページ
<img width="800" alt="スクリーンショット 2021-12-06 22 08 12" src="https://user-images.githubusercontent.com/56378289/151979071-7a8891b1-f48c-4199-a365-90491ceb1f66.png">


<br>
<br>


## ユーザー情報登録ページ
<img width="800" alt="スクリーンショット 2021-12-09 22 41 36" src="https://user-images.githubusercontent.com/56378289/151979185-975770a7-dc9d-4588-b787-2ac2486cd8bc.png">


<br>
<br>


## ユーザーページ
<img width="800" src="https://user-images.githubusercontent.com/56378289/151979330-4a5662be-6cd8-426a-beac-d1bc2d69874e.png">

