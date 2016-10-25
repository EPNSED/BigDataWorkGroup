/*Copyright [2016] [Neranjan Suranga Edirisinghe, epnsed@gmail.com]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.*/

/*

To compile
sbt update
sbt compile
sbt package

Succesfull compilation will results in target/scala-2.10/simple-project_2.10-1.0.jar. 
This file can be directly submitted in to spark using following command

spark-submit --packages com.databricks:spark-csv_2.10:1.5.0 --class "SimpleApp" --master yarn --deploy-mode cluster --driver-memory 4g --executor-memory 4g --executor-cores 4 target/scala-2.10/simple-project_2.10-1.0.jar


*/


name := "Simple Project"
version := "1.0"
scalaVersion := "2.10.4"
libraryDependencies += "org.apache.spark" %% "spark-core" % "1.5.2"
libraryDependencies += "org.apache.spark" %% "spark-sql" % "1.5.2"
libraryDependencies += "com.databricks" %% "spark-csv" % "1.5.0"
