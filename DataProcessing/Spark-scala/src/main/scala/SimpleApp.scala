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
/*SimpleApp.scala*/
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
object SimpleApp {
def main(args: Array[String]) {
 val conf = new SparkConf().setAppName("Simple Application")
 val sc = new SparkContext(conf)
 val sqlContext = new SQLContext(sc)
 val df = sqlContext.read.format("com.databricks.spark.csv").option("header","true").option("inferSchema","true").load("hdfs://dicenode02.rs.gsu.edu:8020/user/appadmin/Eventbrite/Data.csv")
 val Results = df.groupBy("category").count()
 Results.write.format("com.databricks.spark.csv").save("hdfs://dicenode02.rs.gsu.edu:8020/user/appadmin/Eventbrite/Result.csv")
}
}
